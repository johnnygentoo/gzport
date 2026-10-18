// SPDX-License-Identifier: GPL-2.0-or-later
// libSceRudp for online play: reliable, ordered messages between two players over a P2P socket
// (sceNetSocket type DGRAM_P2P, carried by the module's shared UDP transport). GODZILLA's versus
// mode sends its match over it: one context per opponent, bound to its P2P socket (vport 778) and
// initiated to the address signaling gave, read packet by packet (1 KiB at most), flushed and
// terminated at the end of the match, then the socket closed once the library releases it.
//
// Both players run this library, so the wire format is its own (not Sony's): a small header on
// each datagram, a simultaneous open (each side sends SYN until it hears the other), sequence
// numbers with cumulative acks and retransmission, keep-alive pings and a FIN. Every callback into
// the game comes from the library's IO thread (a guest thread), never from inside a call the game
// makes: the game holds its own locks around sceRudpWrite and its handlers take them again.

#include <arpa/inet.h>

#include <algorithm>
#include <chrono>
#include <cstdlib>
#include <cstring>
#include <deque>
#include <map>
#include <mutex>
#include <random>
#include <thread>
#include <vector>

#include "common/logging/log.h"
#include "common/types.h"
#include "core/libraries/kernel/threads/pthread.h"
#include "core/libraries/libs.h"
#include "core/libraries/network/net.h"
#include "core/libraries/np/np_common.h"

namespace Libraries::Rudp {
namespace {
using Clock = std::chrono::steady_clock;
using Ms = std::chrono::milliseconds;

// Error codes (SCE_RUDP_ERROR_*), the ones the game tests among them: WOULDBLOCK from a write
// is not an error to it, IN_PROGRESS from a flush means "again later", NOT_ACCEPTABLE ends it.
constexpr s32 ErrorNotInitialized = s32(0x80770001);
constexpr s32 ErrorAlreadyInitialized = s32(0x80770002);
constexpr s32 ErrorInvalidContextId = s32(0x80770003);
constexpr s32 ErrorInvalidArgument = s32(0x80770004);
constexpr s32 ErrorInvalidOption = s32(0x80770005);
constexpr s32 ErrorConnectionReset = s32(0x80770009);
constexpr s32 ErrorConnectionTimeout = s32(0x8077000B);
constexpr s32 ErrorThread = s32(0x8077000F);
constexpr s32 ErrorNotAcceptable = s32(0x80770011);
constexpr s32 ErrorMessageTooLarge = s32(0x80770012);
constexpr s32 ErrorNotBound = s32(0x80770013);
constexpr s32 ErrorWouldBlock = s32(0x80770016);
constexpr s32 ErrorAlreadyBound = s32(0x8077001D);
constexpr s32 ErrorTooManyContexts = s32(0x80770020);
constexpr s32 ErrorKeepAliveFailure = s32(0x80770026);

// Context events (the game's handler: 1 closed, 2 established, 3 error with a code, 6 flushed).
constexpr s32 EventClosed = 1;
constexpr s32 EventEstablished = 2;
constexpr s32 EventError = 3;
constexpr s32 EventFlushed = 6;
// The library's event: the socket of the last context terminated is the game's again (it waits
// for this before closing it).
constexpr s32 EventSocketReleased = 2;

// Options (sceRudpSetOption): the game sets the connection timeout (ms).
constexpr s32 OptionConnectionTimeout = 9;
constexpr s32 OptionKeepAliveTimeout = 19;

using ContextHandler = void PS4_SYSV_ABI (*)(s32 context, s32 event, s32 error, void* arg);
using EventHandler = s32 PS4_SYSV_ABI (*)(s32 event, s32 socket, const u8* data, u64 size,
                                          const Net::OrbisNetSockaddr* address, u32 length,
                                          void* arg);

// The datagram header. Sessions tell this connection's packets from a previous one's.
constexpr u32 Magic = 0x55525a47; // "GZRU"
enum PacketType : u8 { Syn = 1, SynReply = 2, Data = 3, Ack = 4, Ping = 5, Fin = 6 };
#pragma pack(push, 1)
struct Header {
    u32 magic;
    u8 type;
    u8 reserved[3];
    u32 sender;   // the sender's session
    u32 receiver; // the receiver's session (0 until known)
    u32 sequence; // Data: its number, from 1
    u32 ack;      // every packet: the last number received in order
};
#pragma pack(pop)
constexpr u32 MaxPayload = 1200; // well under the transport's datagram limit
constexpr u32 MaxUnacked = 512;  // then writes would block
constexpr u32 MaxEarly = 512;    // out-of-order packets kept for later
constexpr int MaxContexts = 32;

enum class State { Created, Bound, Opening, Established, Closed };

struct Outgoing {
    u32 sequence;
    std::vector<u8> datagram;
    Clock::time_point sent;
    Clock::time_point first_sent;
    bool retransmitted = false;
};

struct Context {
    ContextHandler handler = nullptr;
    void* arg = nullptr;
    State state = State::Created;
    s32 socket = -1;
    Net::OrbisNetSockaddrIn peer{};
    u32 session = 0;
    u32 peer_session = 0;
    Ms connection_timeout{30000};
    Ms keep_alive_timeout{10000};
    Clock::time_point deadline{};      // the open's, while Opening
    Clock::time_point last_received{}; // anything from the peer
    Clock::time_point last_sent{};
    Clock::time_point last_syn{};
    // Sending.
    u32 next_sequence = 1;
    std::deque<Outgoing> unacked;
    Ms rto{100};
    double srtt_ms = 0.0;
    bool flush_pending = false;
    // Receiving.
    u32 received = 0; // the last number delivered in order
    std::map<u32, std::vector<u8>> early;
    std::deque<std::vector<u8>> readable;
    bool ack_due = false;
};

struct PendingEvent {
    bool context; // else the library's event
    s32 id;       // context or socket
    s32 event;
    s32 error;
    ContextHandler context_handler;
    void* arg;
};

struct Library {
    std::mutex mutex;
    bool initialized = false;
    EventHandler handler = nullptr;
    void* handler_arg = nullptr;
    std::map<s32, Context> contexts;
    s32 next_id = 1;
    std::vector<PendingEvent> events;
    Libraries::Kernel::PthreadT thread = nullptr;
    bool running = false;
    std::mt19937 random{std::random_device{}()};
    u32 drop_percent = 0; // BB_RUDP_DROP: datagrams lost on purpose (tests)
} g;

bool SamePeer(const Net::OrbisNetSockaddrIn& a, const Net::OrbisNetSockaddrIn& b) {
    return a.sin_addr == b.sin_addr && a.sin_port == b.sin_port && a.sin_vport == b.sin_vport;
}

std::vector<u8> Datagram(const Context& c, PacketType type, u32 sequence, const void* payload,
                         u32 size) {
    std::vector<u8> out(sizeof(Header) + size);
    const Header h{Magic, type, {}, c.session, c.peer_session, sequence, c.received};
    std::memcpy(out.data(), &h, sizeof(h));
    if (size) {
        std::memcpy(out.data() + sizeof(h), payload, size);
    }
    return out;
}

void Send(Context& c, const std::vector<u8>& datagram) {
    if (c.socket < 0) {
        return;
    }
    if (g.drop_percent && g.random() % 100 < g.drop_percent) {
        c.last_sent = Clock::now();
        c.ack_due = false;
        return;
    }
    Net::sceNetSendto(c.socket, datagram.data(), datagram.size(), 0,
                      reinterpret_cast<const Net::OrbisNetSockaddr*>(&c.peer), sizeof(c.peer));
    c.last_sent = Clock::now();
    c.ack_due = false;
}

void SendControl(Context& c, PacketType type) {
    Send(c, Datagram(c, type, 0, nullptr, 0));
}

void Post(s32 id, Context& c, s32 event, s32 error) {
    g.events.push_back({true, id, event, error, c.handler, c.arg});
}

void Fail(s32 id, Context& c, s32 error) {
    LOG_WARNING(Lib_Rudp, "context {}: error {:#x}", id, static_cast<u32>(error));
    c.state = State::Closed;
    c.unacked.clear();
    Post(id, c, EventError, error);
}

void Establish(s32 id, Context& c, u32 peer_session) {
    c.peer_session = peer_session;
    if (c.state == State::Opening) {
        c.state = State::Established;
        LOG_INFO(Lib_Rudp, "context {}: connected", id);
        Post(id, c, EventEstablished, 0);
    }
}

void Acknowledged(s32 id, Context& c, u32 ack) {
    const auto now = Clock::now();
    while (!c.unacked.empty() && c.unacked.front().sequence <= ack) {
        const Outgoing& o = c.unacked.front();
        if (!o.retransmitted) { // Karn: only first transmissions measure the round trip
            const double sample = std::chrono::duration<double, std::milli>(now - o.sent).count();
            c.srtt_ms = c.srtt_ms == 0.0 ? sample : c.srtt_ms * 0.875 + sample * 0.125;
            c.rto = Ms(std::clamp(static_cast<int>(c.srtt_ms * 2.0) + 10, 20, 500));
        }
        c.unacked.pop_front();
    }
    if (c.flush_pending && c.unacked.empty()) {
        c.flush_pending = false;
        Post(id, c, EventFlushed, 0);
    }
}

void Receive(s32 id, Context& c, const Header& h, const u8* payload, u32 size) {
    c.last_received = Clock::now();
    switch (h.type) {
    case Syn:
        if (c.state == State::Established && c.peer_session && h.sender != c.peer_session) {
            Fail(id, c, ErrorConnectionReset); // the other player started over
            return;
        }
        Establish(id, c, h.sender);
        SendControl(c, SynReply);
        return;
    case SynReply:
        if (c.state == State::Established && c.peer_session && h.sender != c.peer_session) {
            return;
        }
        Establish(id, c, h.sender);
        return;
    default:
        break;
    }
    if (h.receiver != c.session) {
        return; // for an earlier connection
    }
    if (c.state == State::Opening) {
        Establish(id, c, h.sender); // its SYN reply was lost, its data says it heard us
    }
    if (h.sender != c.peer_session || c.state != State::Established) {
        return;
    }
    Acknowledged(id, c, h.ack);
    switch (h.type) {
    case Data:
        if (h.sequence > c.received && h.sequence <= c.received + MaxEarly) {
            c.early.emplace(h.sequence, std::vector<u8>(payload, payload + size));
            for (auto it = c.early.find(c.received + 1); it != c.early.end();
                 it = c.early.find(c.received + 1)) {
                c.readable.push_back(std::move(it->second));
                c.early.erase(it);
                ++c.received;
            }
        }
        c.ack_due = true; // duplicates too: our ack was lost
        return;
    case Ping:
        c.ack_due = true;
        return;
    case Fin:
        LOG_INFO(Lib_Rudp, "context {}: closed by the other player", id);
        c.state = State::Closed;
        c.unacked.clear();
        Post(id, c, EventClosed, 0);
        return;
    default:
        return;
    }
}

void Dispatch(s32 socket, const Net::OrbisNetSockaddrIn& from, const u8* data, u32 size) {
    if (size < sizeof(Header)) {
        return;
    }
    Header h;
    std::memcpy(&h, data, sizeof(h));
    if (h.magic != Magic) {
        return;
    }
    for (auto& [id, c] : g.contexts) {
        if (c.socket == socket && c.state != State::Closed && c.state >= State::Opening &&
            SamePeer(c.peer, from)) {
            Receive(id, c, h, data + sizeof(h), size - sizeof(h));
            return;
        }
    }
}

void Tick(s32 id, Context& c, Clock::time_point now) {
    if (c.state == State::Opening) {
        if (now >= c.deadline) {
            Fail(id, c, ErrorConnectionTimeout);
            return;
        }
        if (now - c.last_syn >= Ms(100)) {
            c.last_syn = now;
            SendControl(c, Syn);
        }
        return;
    }
    if (c.state != State::Established) {
        return;
    }
    if (now - c.last_received >= c.keep_alive_timeout) {
        Fail(id, c, ErrorKeepAliveFailure);
        return;
    }
    for (Outgoing& o : c.unacked) {
        if (now - o.first_sent >= c.connection_timeout) {
            Fail(id, c, ErrorConnectionTimeout);
            return;
        }
        if (now - o.sent >= c.rto) {
            // The ack field is refreshed: the copy goes out with what we have received since.
            Header h;
            std::memcpy(&h, o.datagram.data(), sizeof(h));
            h.ack = c.received;
            std::memcpy(o.datagram.data(), &h, sizeof(h));
            Send(c, o.datagram);
            o.sent = now;
            o.retransmitted = true;
        }
    }
    if (c.ack_due) {
        SendControl(c, Ack);
    } else if (now - c.last_sent >= Ms(500)) {
        SendControl(c, Ping);
    }
}

void* PS4_SYSV_ABI IoThread(void*) {
    std::vector<u8> buffer(2048);
    std::vector<PendingEvent> events;
    for (;;) {
        {
            std::scoped_lock lock(g.mutex);
            if (!g.running) {
                break;
            }
            std::vector<s32> sockets;
            for (const auto& [id, c] : g.contexts) {
                if (c.socket >= 0 && std::find(sockets.begin(), sockets.end(), c.socket) ==
                                         sockets.end()) {
                    sockets.push_back(c.socket);
                }
            }
            for (const s32 socket : sockets) {
                for (int i = 0; i < 256; ++i) {
                    Net::OrbisNetSockaddrIn from{};
                    u32 length = sizeof(from);
                    const int got = Net::sceNetRecvfrom(
                        socket, buffer.data(), buffer.size(), Net::ORBIS_NET_MSG_DONTWAIT,
                        reinterpret_cast<Net::OrbisNetSockaddr*>(&from), &length);
                    if (got < 0) {
                        break;
                    }
                    Dispatch(socket, from, buffer.data(), static_cast<u32>(got));
                }
            }
            const auto now = Clock::now();
            for (auto& [id, c] : g.contexts) {
                Tick(id, c, now);
            }
            events.swap(g.events);
        }
        // Outside the lock: the handlers call back into the library.
        for (const PendingEvent& e : events) {
            if (e.context) {
                if (e.context_handler) {
                    e.context_handler(e.id, e.event, e.error, e.arg);
                }
            } else if (g.handler) {
                g.handler(e.event, e.id, nullptr, 0, nullptr, 0, g.handler_arg);
            }
        }
        events.clear();
        std::this_thread::sleep_for(Ms(1));
    }
    return nullptr;
}

s32 StartThread() {
    if (g.running) {
        return 0;
    }
    g.running = true;
    const s32 rc = Np::NpCommon::sceNpCreateThread(&g.thread, IoThread, nullptr, 700, 0x4000, 0,
                                                   "SceRudpIo");
    if (rc < 0) {
        g.running = false;
        g.thread = nullptr;
        LOG_ERROR(Lib_Rudp, "IO thread did not start: {:#x}", static_cast<u32>(rc));
        return ErrorThread;
    }
    return 0;
}

Context* Find(s32 id) {
    const auto it = g.contexts.find(id);
    return it == g.contexts.end() ? nullptr : &it->second;
}

/// The socket's last context is gone: the library lets go of it.
void ReleaseSocket(s32 socket) {
    for (const auto& [id, c] : g.contexts) {
        if (c.socket == socket) {
            return;
        }
    }
    g.events.push_back({false, socket, EventSocketReleased, 0, nullptr, nullptr});
}
} // namespace

s32 PS4_SYSV_ABI sceRudpInit(void* pool, s32 size) {
    std::scoped_lock lock(g.mutex);
    if (g.initialized) {
        return ErrorAlreadyInitialized;
    }
    (void)pool; // the host's heap holds the library's state
    (void)size;
    g.initialized = true;
    const char* drop = std::getenv("BB_RUDP_DROP");
    g.drop_percent = drop ? std::min(std::atoi(drop), 90) : 0;
    LOG_INFO(Lib_Rudp, "initialized");
    return StartThread();
}

s32 PS4_SYSV_ABI sceRudpEnd() {
    Libraries::Kernel::PthreadT thread = nullptr;
    {
        std::scoped_lock lock(g.mutex);
        if (!g.initialized) {
            return ErrorNotInitialized;
        }
        for (auto& [id, c] : g.contexts) {
            if (c.state == State::Established) {
                SendControl(c, Fin);
            }
        }
        g.contexts.clear();
        g.events.clear();
        g.handler = nullptr;
        g.initialized = false;
        g.running = false;
        thread = g.thread;
        g.thread = nullptr;
    }
    if (thread) {
        Np::NpCommon::sceNpJoinThread(thread, nullptr);
    }
    return 0;
}

s32 PS4_SYSV_ABI sceRudpEnableInternalIOThread(u32 stack_size, u32 priority) {
    (void)stack_size;
    (void)priority;
    std::scoped_lock lock(g.mutex);
    return g.initialized ? StartThread() : ErrorNotInitialized;
}

s32 PS4_SYSV_ABI sceRudpSetEventHandler(EventHandler handler, void* arg) {
    std::scoped_lock lock(g.mutex);
    if (!g.initialized) {
        return ErrorNotInitialized;
    }
    g.handler = handler;
    g.handler_arg = arg;
    return 0;
}

s32 PS4_SYSV_ABI sceRudpCreateContext(ContextHandler handler, void* arg, s32* id) {
    std::scoped_lock lock(g.mutex);
    if (!g.initialized) {
        return ErrorNotInitialized;
    }
    if (!id) {
        return ErrorInvalidArgument;
    }
    if (g.contexts.size() >= MaxContexts) {
        return ErrorTooManyContexts;
    }
    const s32 context_id = g.next_id++;
    Context& c = g.contexts[context_id];
    c.handler = handler;
    c.arg = arg;
    do {
        c.session = g.random();
    } while (c.session == 0);
    *id = context_id;
    return 0;
}

s32 PS4_SYSV_ABI sceRudpSetOption(s32 id, s32 option, const void* value, u64 size) {
    std::scoped_lock lock(g.mutex);
    Context* c = Find(id);
    if (!c) {
        return ErrorInvalidContextId;
    }
    if (!value) {
        return ErrorInvalidArgument;
    }
    if (option == OptionConnectionTimeout || option == OptionKeepAliveTimeout) {
        if (size != sizeof(u32)) {
            return ErrorInvalidOption;
        }
        u32 ms;
        std::memcpy(&ms, value, sizeof(ms));
        (option == OptionConnectionTimeout ? c->connection_timeout : c->keep_alive_timeout) =
            Ms(std::max<u32>(ms, 1000));
    }
    return 0; // the others (buffers, no-delay, criticality) change nothing here
}

s32 PS4_SYSV_ABI sceRudpBind(s32 id, s32 socket, u16 vport, u8 mux_mode) {
    (void)vport; // the socket's own vport carries the packets
    (void)mux_mode;
    std::scoped_lock lock(g.mutex);
    Context* c = Find(id);
    if (!c) {
        return ErrorInvalidContextId;
    }
    if (c->state != State::Created) {
        return ErrorAlreadyBound;
    }
    c->socket = socket;
    c->state = State::Bound;
    return 0;
}

s32 PS4_SYSV_ABI sceRudpInitiate(s32 id, const Net::OrbisNetSockaddr* to, u32 length, s32 flags) {
    (void)flags;
    std::scoped_lock lock(g.mutex);
    Context* c = Find(id);
    if (!c) {
        return ErrorInvalidContextId;
    }
    if (!to || length < sizeof(Net::OrbisNetSockaddrIn)) {
        return ErrorInvalidArgument;
    }
    if (c->state != State::Bound) {
        return c->state == State::Created ? ErrorNotBound : ErrorNotAcceptable;
    }
    std::memcpy(&c->peer, to, sizeof(c->peer));
    const auto now = Clock::now();
    c->state = State::Opening;
    c->deadline = now + c->connection_timeout;
    c->last_received = now;
    c->last_syn = now;
    const u32 address = c->peer.sin_addr;
    const u8* a = reinterpret_cast<const u8*>(&address);
    LOG_INFO(Lib_Rudp, "context {}: connecting to {}.{}.{}.{}:{} vport {}", id, a[0], a[1], a[2],
             a[3], ntohs(c->peer.sin_port), ntohs(c->peer.sin_vport));
    SendControl(*c, Syn);
    return 0;
}

s32 PS4_SYSV_ABI sceRudpTerminate(s32 id) {
    std::scoped_lock lock(g.mutex);
    Context* c = Find(id);
    if (!c) {
        return ErrorInvalidContextId;
    }
    if (c->state == State::Established) {
        for (int i = 0; i < 5; ++i) { // no answer comes; if all are lost, keep-alive ends it
            SendControl(*c, Fin);
        }
    }
    const s32 socket = c->socket;
    g.contexts.erase(id);
    if (socket >= 0) {
        ReleaseSocket(socket);
    }
    return 0;
}

s32 PS4_SYSV_ABI sceRudpWrite(s32 id, const void* data, u64 size, u8 flags) {
    (void)flags;
    std::scoped_lock lock(g.mutex);
    Context* c = Find(id);
    if (!c) {
        return ErrorInvalidContextId;
    }
    if (c->state != State::Established) {
        return ErrorNotAcceptable;
    }
    if (!data && size) {
        return ErrorInvalidArgument;
    }
    if (size > MaxPayload) {
        return ErrorMessageTooLarge;
    }
    if (c->unacked.size() >= MaxUnacked) {
        return ErrorWouldBlock;
    }
    const auto now = Clock::now();
    const u32 sequence = c->next_sequence++;
    Outgoing o{sequence, Datagram(*c, Data, sequence, data, static_cast<u32>(size)), now, now};
    Send(*c, o.datagram);
    c->unacked.push_back(std::move(o));
    return static_cast<s32>(size);
}

s32 PS4_SYSV_ABI sceRudpRead(s32 id, void* data, u64 size, u8 flags, void* info) {
    (void)flags;
    (void)info;
    std::scoped_lock lock(g.mutex);
    Context* c = Find(id);
    if (!c) {
        return ErrorInvalidContextId;
    }
    if (c->readable.empty()) {
        return c->state == State::Established || c->state == State::Opening
                   ? ErrorWouldBlock
                   : ErrorNotAcceptable;
    }
    if (!data && size) {
        return ErrorInvalidArgument;
    }
    const std::vector<u8>& message = c->readable.front();
    const u64 amount = std::min<u64>(size, message.size());
    if (amount) {
        std::memcpy(data, message.data(), amount);
    }
    c->readable.pop_front();
    return static_cast<s32>(amount);
}

s32 PS4_SYSV_ABI sceRudpGetNumberOfPacketsToRead(s32 id) {
    std::scoped_lock lock(g.mutex);
    const Context* c = Find(id);
    return c ? static_cast<s32>(c->readable.size()) : ErrorInvalidContextId;
}

s32 PS4_SYSV_ABI sceRudpGetSizeReadable(s32 id) {
    std::scoped_lock lock(g.mutex);
    const Context* c = Find(id);
    if (!c) {
        return ErrorInvalidContextId;
    }
    u64 total = 0;
    for (const auto& message : c->readable) {
        total += message.size();
    }
    return static_cast<s32>(total);
}

/// Everything written goes out at once: a flush waits only for the acks (event FLUSHED).
s32 PS4_SYSV_ABI sceRudpFlush(s32 id) {
    std::scoped_lock lock(g.mutex);
    Context* c = Find(id);
    if (!c) {
        return ErrorInvalidContextId;
    }
    if (c->state != State::Established) {
        return ErrorNotAcceptable;
    }
    c->flush_pending = true;
    if (c->unacked.empty()) {
        c->flush_pending = false;
        Post(id, *c, EventFlushed, 0);
    }
    return 0;
}

s32 PS4_SYSV_ABI sceRudpNetFlush() {
    std::scoped_lock lock(g.mutex);
    return g.initialized ? 0 : ErrorNotInitialized;
}

void RegisterLib(Core::Loader::SymbolsResolver* sym) {
    LIB_FUNCTION("amuBfI-AQc4", "libSceRudp", 1, "libSceRudp", sceRudpInit);
    LIB_FUNCTION("3hBvwqEwqj8", "libSceRudp", 1, "libSceRudp", sceRudpEnd);
    LIB_FUNCTION("6PBNpsgyaxw", "libSceRudp", 1, "libSceRudp", sceRudpEnableInternalIOThread);
    LIB_FUNCTION("SUEVes8gvmw", "libSceRudp", 1, "libSceRudp", sceRudpSetEventHandler);
    LIB_FUNCTION("CAbbX6BuQZ0", "libSceRudp", 1, "libSceRudp", sceRudpCreateContext);
    LIB_FUNCTION("0yzYdZf0IwE", "libSceRudp", 1, "libSceRudp", sceRudpSetOption);
    LIB_FUNCTION("l4SLBpKUDK4", "libSceRudp", 1, "libSceRudp", sceRudpBind);
    LIB_FUNCTION("szEVu+edXV4", "libSceRudp", 1, "libSceRudp", sceRudpInitiate);
    LIB_FUNCTION("OMYRTU0uc4w", "libSceRudp", 1, "libSceRudp", sceRudpTerminate);
    LIB_FUNCTION("KaPL3fbTLCA", "libSceRudp", 1, "libSceRudp", sceRudpWrite);
    LIB_FUNCTION("rZqWV3eXgOA", "libSceRudp", 1, "libSceRudp", sceRudpRead);
    LIB_FUNCTION("Px0miD2LuW0", "libSceRudp", 1, "libSceRudp", sceRudpGetNumberOfPacketsToRead);
    LIB_FUNCTION("sAZqO2+5Qqo", "libSceRudp", 1, "libSceRudp", sceRudpGetSizeReadable);
    LIB_FUNCTION("Ms0cLK8sTtE", "libSceRudp", 1, "libSceRudp", sceRudpFlush);
    LIB_FUNCTION("+BJ9svDmjYs", "libSceRudp", 1, "libSceRudp", sceRudpNetFlush);
}

} // namespace Libraries::Rudp

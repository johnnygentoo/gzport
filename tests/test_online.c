#define _GNU_SOURCE
#include "runtime.h"
#include "gpu/bbgpu.h"
#include "gpu/bbnet/bbnet.h"
#include <assert.h>
#include <dlfcn.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <arpa/inet.h>
#include <stdatomic.h>
#include <time.h>

/* The settings menu of the GPU library restarts through probe.c, which tests do not link. */
void runtime_restart(void) { abort(); }

/* ---- Rudp (GODZILLA's versus matches): two contexts in this process, each on its own P2P
 * socket, reach each other through the module's UDP transport on the loopback. ---- */
typedef struct { uint8_t len, family; uint16_t port; uint32_t addr; uint16_t vport; char zero[6]; } P2PAddress;
typedef int32_t (*SocketFn)(const char *,int,int,int);
typedef int32_t (*BindFn)(int32_t,const void *,uint32_t);
typedef int32_t (*CloseFn)(int32_t);
typedef void (*ContextHandler)(int32_t,int32_t,int32_t,void *);
typedef int32_t (*EventHandler)(int32_t,int32_t,const uint8_t *,uint64_t,const void *,uint32_t,void *);
typedef int32_t (*InitFn)(void *,int32_t);
typedef int32_t (*VoidFn)(void);
typedef int32_t (*ThreadFn)(uint32_t,uint32_t);
typedef int32_t (*SetEventHandlerFn)(EventHandler,void *);
typedef int32_t (*CreateFn)(ContextHandler,void *,int32_t *);
typedef int32_t (*OptionFn)(int32_t,int32_t,const void *,uint64_t);
typedef int32_t (*RudpBindFn)(int32_t,int32_t,uint16_t,uint8_t);
typedef int32_t (*InitiateFn)(int32_t,const void *,uint32_t,int32_t);
typedef int32_t (*ContextFn)(int32_t);
typedef int32_t (*WriteFn)(int32_t,const void *,uint64_t,uint8_t);
typedef int32_t (*ReadFn)(int32_t,void *,uint64_t,uint8_t,void *);

typedef struct { atomic_int established, closed, errors, flushed; } Peer;
static atomic_int released;
static void context_event(int32_t context,int32_t event,int32_t error,void *arg) {
    (void)context; (void)error;
    Peer *peer=arg;
    if (event==1) atomic_fetch_add(&peer->closed,1);
    if (event==2) atomic_fetch_add(&peer->established,1);
    if (event==3) atomic_fetch_add(&peer->errors,1);
    if (event==6) atomic_fetch_add(&peer->flushed,1);
}
static int32_t library_event(int32_t event,int32_t socket,const uint8_t *data,uint64_t size,const void *address,uint32_t length,void *arg) {
    (void)socket; (void)data; (void)size; (void)address; (void)length; (void)arg;
    if (event==2) atomic_fetch_add(&released,1);
    return 0;
}
static void pause_ms(int ms) { struct timespec t={ms/1000,(ms%1000)*1000000L}; nanosleep(&t,NULL); }
static int wait_for(atomic_int *value,int at_least) {
    for (int i=0;i<10000 && atomic_load(value)<at_least;++i) pause_ms(1);
    return atomic_load(value)>=at_least;
}
static void *need(BbNetResolveFn resolve,const char *nid) {
    void *address=(void *)resolve(nid);
    if (!address) { printf("FAIL: the online module has no %s\n",nid); exit(1); }
    return address;
}

static int rudp_exchange(BbNetResolveFn resolve,uint16_t port,int drop) {
    const SocketFn net_socket=need(resolve,"Q4qBuN-c0ZM");
    const BindFn net_bind=need(resolve,"bErx49PgxyY");
    const CloseFn net_close=need(resolve,"45ggEzakPJQ");
    const InitFn init=need(resolve,"amuBfI-AQc4");
    const VoidFn end=need(resolve,"3hBvwqEwqj8");
    const ThreadFn io_thread=need(resolve,"6PBNpsgyaxw");
    const SetEventHandlerFn set_handler=need(resolve,"SUEVes8gvmw");
    const CreateFn create=need(resolve,"CAbbX6BuQZ0");
    const OptionFn option=need(resolve,"0yzYdZf0IwE");
    const RudpBindFn bind=need(resolve,"l4SLBpKUDK4");
    const InitiateFn initiate=need(resolve,"szEVu+edXV4");
    const ContextFn terminate=need(resolve,"OMYRTU0uc4w");
    const WriteFn write=need(resolve,"KaPL3fbTLCA");
    const ReadFn read=need(resolve,"rZqWV3eXgOA");
    const ContextFn packets=need(resolve,"Px0miD2LuW0");
    const ContextFn flush=need(resolve,"Ms0cLK8sTtE");
    static uint8_t pool[0x20000];
    char percent[8];
    snprintf(percent,sizeof(percent),"%d",drop);
    setenv("BB_RUDP_DROP",percent,1);
    atomic_store(&released,0);
    assert(init(pool,sizeof(pool))==0);
    assert(set_handler(library_event,NULL)==0);
    assert(io_thread(0x4000,700)==0);
    /* As the game does: a P2P socket on vport 778 (here a second one on 779 is the other player). */
    int32_t sockets[2];
    P2PAddress local[2];
    for (int i=0;i<2;++i) {
        sockets[i]=net_socket("rudp",2,6,0);
        if (sockets[i]<0) { printf("FAIL: no P2P socket (%#x)\n",(unsigned)sockets[i]); return 1; }
        memset(&local[i],0,sizeof(local[i]));
        local[i].len=sizeof(local[i]); local[i].family=2;
        local[i].port=htons(port); local[i].addr=htonl(INADDR_LOOPBACK); local[i].vport=htons((uint16_t)(778+i));
        if (net_bind(sockets[i],&local[i],sizeof(local[i]))<0) { printf("FAIL: P2P bind\n"); return 1; }
    }
    static Peer peers[2];
    memset(peers,0,sizeof(peers));
    int32_t contexts[2];
    for (int i=0;i<2;++i) {
        assert(create(context_event,&peers[i],&contexts[i])==0);
        const uint32_t timeout=30000;
        assert(option(contexts[i],9,&timeout,sizeof(timeout))==0);
        assert(bind(contexts[i],sockets[i],778,1)==0);
    }
    /* Writing before the connection is up is refused. */
    assert(write(contexts[0],"x",1,0)==(int32_t)0x80770011);
    for (int i=0;i<2;++i) assert(initiate(contexts[i],&local[1-i],sizeof(local[i]),0)==0);
    if (!wait_for(&peers[0].established,1) || !wait_for(&peers[1].established,1)) {
        printf("FAIL: the two contexts did not connect\n"); return 1;
    }
    /* Messages keep their boundaries and order, both ways. */
    enum { Count=300 };
    for (int n=0;n<Count;++n) {
        for (int i=0;i<2;++i) {
            uint8_t message[64];
            const int size=1+n%60;
            for (int k=0;k<size;++k) message[k]=(uint8_t)(n+k+i*7);
            assert(write(contexts[i],message,(uint64_t)size,0)==size);
        }
    }
    for (int i=0;i<2;++i) {
        int got=0;
        for (int tries=0;got<Count && tries<10000;++tries) {
            const int32_t waiting=packets(contexts[i]);
            assert(waiting>=0);
            if (!waiting) { pause_ms(1); continue; }
            for (int32_t m=0;m<waiting;++m) {
                uint8_t buffer[0x400];
                const int32_t size=read(contexts[i],buffer,sizeof(buffer),0,NULL);
                const int other=1-i;
                assert(size==1+got%60);
                for (int k=0;k<size;++k) assert(buffer[k]==(uint8_t)(got+k+other*7));
                ++got;
            }
        }
        if (got!=Count) { printf("FAIL: context %d read %d of %d messages\n",i,got,Count); return 1; }
    }
    /* The end of a match: flush (acked: FLUSHED), terminate; the other side hears it closed, and
     * each socket is released once its context is gone. */
    assert(flush(contexts[0])==0);
    if (!wait_for(&peers[0].flushed,1)) { printf("FAIL: no FLUSHED event\n"); return 1; }
    assert(terminate(contexts[0])==0);
    if (!wait_for(&peers[1].closed,1)) { printf("FAIL: the other side was not told of the close\n"); return 1; }
    assert(terminate(contexts[1])==0);
    if (!wait_for(&released,2)) { printf("FAIL: sockets not released\n"); return 1; }
    assert(atomic_load(&peers[0].errors)==0 && atomic_load(&peers[1].errors)==0);
    assert(end()==0);
    for (int i=0;i<2;++i) net_close(sockets[i]);
    printf("PASS: Rudp connects two P2P sockets, keeps %d messages each way in order, flushes and closes (%d%% of datagrams lost)\n",Count,drop);
    return 0;
}

/* Online play (BB_ONLINE=1): the game's network and PSN imports resolve to the online module
 * (out/gpu/libbbnet.so); trophies stay with the runtime. Without the module (a build without its
 * libraries) there is nothing to check. */
int main(void) {
    static const char *const online[]={
        "Nlev7Lg8k3A#E#F",  /* sceNetInit */
        "A9cVMUtEp4Y#K#L",  /* sceHttpInit */
        "hdpVEUDFW3s#L#M",  /* sceSslInit */
        "2rsFmlGWleQ#R#S",  /* sceNpCheckNpAvailability */
        "10t3e5+JPnU#P#Q",  /* sceNpMatching2Initialize */
        "3KOuC4RmZZU#T#U",  /* sceNpSignalingInitialize */
        "amuBfI-AQc4#h#h",  /* sceRudpInit */
    };
    static const char *const local="XbkjbobZlCY#l#m"; /* sceNpTrophyCreateContext */
    const char *path="out/gpu/libbbnet.so";
    void *module=dlopen(path,RTLD_NOW|RTLD_LOCAL); /* the same handle the runtime gets */
    if (!module) {
        printf("SKIP: no online module (%s)\n",dlerror());
        return 0;
    }
    const BbNetResolveFn resolve=(BbNetResolveFn)dlsym(module,"bbnet_resolve");
    assert(resolve);
    setenv("BB_ONLINE","1",1);
    setenv("BB_NET_MODULE",path,1);
    runtime_start(1);
    bbgpu_register_kernel();
    for (size_t i=0;i<sizeof(online)/sizeof(*online);++i) {
        uintptr_t address=runtime_resolve(online[i],0);
        if (!address || address!=resolve(online[i])) {
            printf("FAIL: %s (%s) is not the online version\n",online[i],runtime_import_name(online[i]));
            return 1;
        }
    }
    uintptr_t trophy=runtime_resolve(local,0);
    assert(trophy && trophy!=resolve(local));
    printf("PASS: online imports go to the online module, trophies stay local\n");
    /* A port of its own for the transport: the test may run beside a game. */
    setenv("SHADPS4_P2P_PORT","39658",1);
    return rudp_exchange(resolve,39658,0) || rudp_exchange(resolve,39658,30);
}

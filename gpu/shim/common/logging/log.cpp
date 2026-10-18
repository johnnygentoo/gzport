// bbport: see log.h.
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <mutex>
#include "common/logging/log.h"

namespace Common::Log {
static Level parse(const char* variable, Level fallback) {
    const char* v = std::getenv(variable);
    if (!v) return fallback;
    static const char* names[] = {"trace", "debug", "info", "warning", "error", "critical"};
    for (int i = 0; i < 6; ++i)
        if (!std::strcmp(v, names[i])) return Level(i);
    return fallback;
}
static Level threshold() {
    static const Level level = parse("BB_GPU_LOG", Level::warn);
    return level;
}
static Level net_threshold() {
    static const Level level = parse("BB_NET_LOG", threshold());
    return level;
}
static bool NetClass(std::string_view c) {
    for (std::string_view prefix : {"Lib.Net", "Lib.Np", "Lib.Rudp", "Lib.Http", "Lib.Ssl",
                                    "ShadNet", "NpHandler"})
        if (c.starts_with(prefix)) return true;
    return false;
}
bool ShouldLog(Level level) { return level >= threshold(); }
bool ShouldLog(std::string_view log_class, Level level) {
    return level >= (NetClass(log_class) ? net_threshold() : threshold());
}
void Write(std::string_view log_class, Level level, const char* file, int line, const char* function,
           std::string&& message) {
    static std::mutex mutex;
    static const char* names[] = {"Trace", "Debug", "Info", "Warning", "Error", "Critical"};
    const char* base = std::strrchr(file, '/');
    std::scoped_lock lock{mutex};
    std::fprintf(stderr, "GPU [%.*s] <%s> %s:%d %s: %s\n", int(log_class.size()), log_class.data(),
                 names[int(level)], base ? base + 1 : file, line, function, message.c_str());
}
} // namespace Common::Log

# Documentation

## For players

- [../BUILD.md](../BUILD.md): building gzport, its tests, and what to do when a build fails.
- [LAN-VERSUS.md](LAN-VERSUS.md): versus over the LAN: the server (with its Docker image), the
  accounts, the launcher's **Online** page.
- [DEBUGGING.md](DEBUGGING.md): catching a crash with a debugger.

## bbport's design notes

These come from [bbport](https://github.com/deadinside28/bloodborne_pc) by deadinside28 and
[bloodborne_linux](https://github.com/ayozetr/bloodborne_linux) by ayozetr. They describe the
runtime and the GPU library gzport runs on, so they still apply; their examples and measurements
come from bbport's first game. Many are in Russian (`.ru.md`). bbport's changelogs, roadmap and
session notes are in those projects.

- **Translation and the GPU commands:** [TRANSLATOR_ARCHITECTURE.ru.md](TRANSLATOR_ARCHITECTURE.ru.md),
  [TRANSLATION_GPU_COPY_LABELS.ru.md](TRANSLATION_GPU_COPY_LABELS.ru.md),
  [parallel_gpu.md](parallel_gpu.md).
- **Memory models:** [MEMORY_MODULE_PLAN.ru.md](MEMORY_MODULE_PLAN.ru.md),
  [NVIDIA_MEMORY_MODEL.ru.md](NVIDIA_MEMORY_MODEL.ru.md).
- **Upscaling, TAA and motion vectors:** [upscaler.md](upscaler.md),
  [DEPTH_ADAPTIVE_TAA.md](DEPTH_ADAPTIVE_TAA.md), [motion_vectors.md](motion_vectors.md).

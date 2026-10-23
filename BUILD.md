# Building gzport

gzport builds from source on Linux x86-64 with one script, `build.sh`. The first build takes a
few minutes (the GPU library is compiled with link-time optimization); later builds only redo
what changed. You also need your own dump of the game to play ([LEGAL.md](LEGAL.md)).

## 1. Requirements

- Linux x86-64, GCC or Clang with C++23, CMake 3.24 or newer, Ninja, pkg-config, Python 3.
- A GPU with Vulkan 1.3: AMD or Intel with Mesa, or NVIDIA with NVIDIA's driver.
- Libraries: Vulkan headers and loader, SDL3, FreeType, FFmpeg, Boost, fmt, magic_enum,
  robin-map, xxHash, Vulkan Memory Allocator, glslang, SPIRV-Cross, SPIRV-Headers, Xbyak, Zydis,
  miniz, protobuf, nlohmann-json, OpenSSL, zlib, miniupnpc.
- For the launcher: PyGObject with GTK 4 and libadwaita, and Pillow.
- Fonts the game's text falls back to: Noto Sans and Noto Sans CJK, DejaVu.
- Optional: Rust's `cargo` for the launcher's **Install from PKG** (without it the launcher only
  takes a game folder); Qt 6.8+ with qt6-httpserver and qt6-websockets on the PC that hosts the
  versus server ([docs/LAN-VERSUS.md](docs/LAN-VERSUS.md)).

### Arch Linux, CachyOS, Manjaro, EndeavourOS (tested)

```bash
sudo pacman -S --needed base-devel cmake ninja python python-gobject gtk4 libadwaita sdl3 \
    vulkan-headers vulkan-icd-loader glslang spirv-headers spirv-cross ffmpeg boost fmt \
    robin-map xxhash zydis miniz protobuf nlohmann-json openssl miniupnpc python-pillow \
    freetype2 noto-fonts noto-fonts-cjk ttf-dejavu
paru -S magic_enum vulkan-memory-allocator xbyak      # from the AUR (or yay -S ...)
sudo pacman -S --needed rust                          # optional: Install from PKG
```

Your GPU's Vulkan driver too: `vulkan-radeon` (AMD), `vulkan-intel` (Intel), or `nvidia-utils`
(NVIDIA).

### NixOS, or any distribution with Nix (tested)

Nothing to install: `bash build.sh` enters `shell.nix` by itself and gets every dependency.

### Other distributions

The same libraries under your distribution's names (the `-devel` / `-dev` packages). `build.sh`
checks for `pkg-config --exists vulkan sdl3 freetype2`, `cmake` and `ninja` first and says
what is missing; CMake then names any other library it cannot find. SDL3 is new: if your
distribution does not package it yet, build it from [libsdl.org](https://libsdl.org). Gentoo
works with the same list (this project is developed on it).

## 2. Get the source

```bash
git clone --recursive https://github.com/johnnygentoo/gzport.git gzport
cd gzport
```

`--recursive` fetches the submodules (FSR-Vulkan, Dear ImGui, LibAtrac9). In a checkout made
without it, `build.sh` runs `git submodule update --init --recursive` for you.

## 3. Build

```bash
bash build.sh
```

It builds, in `out/`:

| Output | What it is |
|---|---|
| `out/gpu/libbbgpu.so` | the GPU library: shadPS4's Vulkan renderer and shader recompiler, the upscalers |
| `out/gpu/libbbnet.so` | the online module (versus over the LAN), loaded only when you play online |
| `out/bb-probe` | the runtime that runs the game's own code |
| `out/pkgextract/` | the PKG extractor (only with `cargo`) |

Options (environment variables):

- `BB_LTO=OFF` — no link-time optimization: faster builds while you change code, a slower game.
  Build once more without it before you play, or the next launch rebuilds everything.
- `BB_PGO=generate` / `use` / `off` — profile-guided optimization of the GPU library (by
  default it is used when `pgo/` holds a profile).
- `CC=clang` — another compiler.

`run.sh` and the launcher call `build.sh` before every start, so a `git pull` is all an update
needs.

## 4. Check the build

```bash
bash build.sh --test                      # the runtime's C tests (memory, threads, pad, files, add-ons, online, Rudp)
python3 -m unittest discover -s tests     # the launcher, scripts and translation tests
```

## 5. Run

Prepare your game folder first (the 1.01 update merged into the game; see
[README.md](README.md#1-the-game-folder)), then:

```bash
launcher/bb-launcher.sh               # the launcher
launcher/install-desktop.sh           # optional: a menu entry with its icon
BB_GAME_DIR=/path/to/CUSA02046 bash run.sh   # or the game without the launcher
```

Saves, the shader cache and settings of a source checkout stay in the checkout (`user/`,
`bbport.ini`) and the launcher's settings in `~/.config/gzport-launcher`. All of them are
ignored by git.

## 6. Optional parts

- **AppImage:** `bash build.sh && bash packaging/appimage-sharun.sh` makes
  `dist/GODZILLA-gzport-x86_64.AppImage`, one file for any distribution and the Steam Deck. Build
  it on Arch Linux with `vulkan-radeon`, `vulkan-intel` and `vulkan-tools`: it carries the build
  PC's libraries, so a system compiled for its own CPU (Gentoo's `-march=native`) makes one that
  crashes on other CPUs. FSR 4's assets go in only with `BB_APPIMAGE_FSR4=1` (for your own use;
  published AppImages leave them out). Do not publish an AppImage built in a folder that holds
  your dump or saves: check what it contains.
- **DLSS** (GeForce RTX, NVIDIA driver): `bash tools/build_dlss.sh` once after `build.sh`; it
  downloads what it needs from NVIDIA's DLSS SDK.
- **FSR 4:** `bash tools/fetch_fsr4_assets.sh` downloads the FSR 4 asset set built from AMD's
  open-source FidelityFX SDK into `fsr4_shaders/`; FSR 4.1.1 is built from AMD's own files with
  `tools/fsr4cap/build_assets.sh` ([docs/upscaler.md](docs/upscaler.md)). Neither is part of the
  repository.
- **Versus server:** [docs/LAN-VERSUS.md](docs/LAN-VERSUS.md) and
  [tools/shadnet-server](tools/shadnet-server).

## 7. When the build fails

- *"Need pkg-config with vulkan, sdl3 and freetype2, cmake and ninja"*: install those (section 1).
- *"GPU library build failed"*: the last 40 lines are shown; the whole log is
  `out/gpu-build.log`. A missing header names the library to install.
- *"pkgextract build failed"*: only **Install from PKG** is missing; everything else works.
  The log is `out/pkgextract-build.log`.
- The NVIDIA driver was just updated and the game does not start: reboot, so the loaded driver
  matches the new libraries.
- After an update the FSR-Vulkan patches do not apply: `build.sh` resets that submodule and
  patches it again by itself; if it still fails, run
  `git submodule update --init --recursive --force`.

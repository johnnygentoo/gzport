#!/usr/bin/env bash
# Builds dist/GODZILLA-gzport-x86_64.AppImage without Nix: the port's current build (run
# build.sh first), its scripts and the GTK4 launcher, with every library they load (glibc, Python
# and PyGObject, GTK 4, libadwaita, SDL3, FFmpeg, Mesa's Vulkan drivers) collected from this
# system by quick-sharun (github.com/pkgforge-dev/Anylinux-AppImages). The AppImage then runs on
# other distributions too; build it on an up-to-date Arch Linux (or CachyOS) with the launcher's
# dependencies installed. NVIDIA's driver comes from the host at run time.
# Running it opens the launcher; `--play` starts the game with the launcher's saved settings.
# Data (generated files, saves, bbport.ini): ~/.local/share/gzport (BB_DATA_DIR), apart from
# bbport's own ~/.local/share/bbport.
set -euo pipefail
cd -- "$(dirname -- "$0")/.."
[[ -f out/bb-probe && -f out/gpu/libbbgpu.so ]] || { echo 'Build first: bash build.sh' >&2; exit 1; }
# Mesa's Vulkan drivers come from this system: on a build host with only NVIDIA's driver none went
# in, and the game found no GPU on AMD and Intel ("Failed to enumerate physical devices:
# ErrorInitializationFailed", issue #4). Arch: vulkan-radeon and vulkan-intel.
for driver in radeon intel; do
    [[ -f /usr/share/vulkan/icd.d/${driver}_icd.json ]] || {
        echo "Mesa's $driver Vulkan driver is not installed: pacman -S vulkan-$driver" >&2; exit 1; }
done
# FSR 4's assets (fsr4_shaders, from a third-party build of AMD's FSR 4 source) are left out of the
# package unless BB_APPIMAGE_FSR4=1: a published AppImage does not redistribute them. Without
# them the launcher does not offer FSR 4; FSR 3.1 and TAA remain.
fsr4=
if [[ ${BB_APPIMAGE_FSR4:-0} == 1 ]]; then bash tools/fetch_fsr4_assets.sh; fsr4=fsr4_shaders; fi
root=$PWD
work=$root/out/appimage
appdir=$work/AppDir
rm -rf "$appdir"
mkdir -p "$appdir/bin" "$appdir/share/bbport" "$work/tmp"

# quick-sharun at a fixed revision; it downloads sharun and appimagetool itself (checksummed).
quick_rev=7eead3068c040e3b530aa06fd46522b4a45a62dc
quick_sha=2ae6fc29242b5c45b63f3638fff71cead679c8c41671a2c3970a6947e332470c
quick=$work/quick-sharun.sh
if ! echo "$quick_sha  $quick" | sha256sum -c --status 2>/dev/null; then
    curl -fsSL -o "$quick" \
        "https://raw.githubusercontent.com/pkgforge-dev/Anylinux-AppImages/$quick_rev/useful-tools/quick-sharun.sh"
    echo "$quick_sha  $quick" | sha256sum -c --quiet
fi
chmod +x "$quick"

# The port as run.sh expects it with BB_PREBUILT=1 (same layout as packaging/default.nix):
# share/bbport/{run.sh,scripts,...,bin/bb-probe}; bin/ is the AppImage's own bin directory.
d=$appdir/share/bbport
cp run.sh "$d/"
cp -r scripts patches $fsr4 launcher "$d/"
mkdir -p "$d/tools"
cp -r tools/fsr4cap "$d/tools/"
find "$d" -name __pycache__ -type d -prune -exec rm -rf {} +
ln -s ../../bin "$d/bin"

# The AppImage's main program: the launcher (or, with --play, the game alone).
cat > "$appdir/bin/godzilla" <<'EOF'
#!/bin/sh
# Entry point of the AppImage (AppRun runs it with APPDIR set and APPDIR/bin first on PATH).
export BB_PREBUILT=1
export PYTHON="$APPDIR/bin/python3"
export BB_VULKANINFO="$APPDIR/bin/vulkaninfo"
export BB_DLSS_DIR="$APPDIR/share/bbport/dlss"
export BB_NET_MODULE="$APPDIR/share/bbport/net/libbbnet.so"
[ -x "$APPDIR/bin/pkgextract" ] && export BB_PKGEXTRACT="$APPDIR/bin/pkgextract"
export BB_DATA_DIR="${BB_DATA_DIR:-${XDG_DATA_HOME:-$HOME/.local/share}/gzport}"
mkdir -p "$BB_DATA_DIR"
# deadinside28#172: Steam's Game Mode runs a non-Steam game in pressure-vessel, which points
# Vulkan at its own driver and layer manifests. They are not the user's choice: dropped (kept as
# BB_HOST_* for the log), so sharun registers the package's Mesa and the host's NVIDIA driver as
# anywhere else. The host's gamescope WSI layer, a host library too, is turned off with them.
for name in VK_DRIVER_FILES VK_ICD_FILENAMES VK_ADD_DRIVER_FILES VK_IMPLICIT_LAYER_PATH \
            VK_LAYER_PATH VK_ADD_LAYER_PATH; do
    eval "value=\${$name-}"
    case $value in
    */pressure-vessel/*) export "BB_HOST_$name=$value"; unset "$name"; pressure_vessel=1 ;;
    esac
done
[ -n "${pressure_vessel-}" ] && export DISABLE_GAMESCOPE_WSI=1
exec "$APPDIR/bin/python3" "$APPDIR/share/bbport/launcher/bbport_launcher.py" "$@"
EOF
chmod +x "$appdir/bin/godzilla"
sed -e 's|@LAUNCHER@|godzilla|' -e 's|@ICON@|godzilla|' \
    launcher/io.github.gzport.Launcher.desktop.in > "$work/godzilla.desktop"
# The AppImage's icon: the launcher's own (launcher/godzilla.svg), as a PNG when librsvg can draw it.
icon=$root/launcher/godzilla.svg
if command -v rsvg-convert >/dev/null; then
    rsvg-convert -w 256 -h 256 "$icon" -o "$work/godzilla.png" && icon=$work/godzilla.png
fi

# GTK, libadwaita and their typelibs are loaded by PyGObject at run time (not linked): named here.
# So are Python's ssl and hashlib modules, which quick-sharun leaves out by default: the launcher's
# connection test and the online module talk HTTPS to servers. Pillow (in site-packages,
# copied with Python) is named too, for the libraries its modules link (keyboard prompts).
pydyn=$(python3 -c 'import sysconfig; print(sysconfig.get_path("platstdlib"))')/lib-dynload
pil=$(python3 -c 'import os, PIL; print(os.path.dirname(PIL.__file__))')
cd "$work"
export APPDIR=$appdir TMPDIR=$work/tmp OUTPATH=$work
export MAIN_BIN=godzilla DESKTOP=$work/godzilla.desktop ICON=$icon
export DEPLOY_PYTHON=1 DEPLOY_GTK=1 GTK_DIR=gtk-4.0 DEPLOY_SDL=1 DEPLOY_VULKAN=1 DEPLOY_PIPEWIRE=1
# Strace mode starts the programs to find what they dlopen: the game needs its game files.
export STRACE_MODE=0
# The AppDir first, the AppImage once the build host's NVIDIA driver is out of it (below).
export OUTPUT_APPIMAGE=0
# The online module (gpu/bbnet), when the build has it: named so that its libraries (protobuf,
# OpenSSL, miniupnpc) come along; the runtime dlopens it at BB_NET_MODULE (below).
net=$(ls "$root/out/gpu/libbbnet.so" 2>/dev/null || true)
# Install from PKG (scripts/pkg_install.py): pkgextract (Unlicense), when the build has it.
pkgextract=$(ls "$root/out/pkgextract/bin/pkgextract" 2>/dev/null || true)
"$quick" \
    "$root/out/bb-probe" "$root/out/bb-gpu-capabilities" ${net:+"$net"} ${pkgextract:+"$pkgextract"} \
    "$(command -v python3)" "$(command -v vulkaninfo)" \
    /usr/lib/libgtk-4.so* /usr/lib/libadwaita-1.so* /usr/lib/libgirepository-*.so* \
    "$pydyn"/_ssl.*.so "$pydyn"/_hashlib.*.so "$pil"/_imaging.*.so "$pil"/_imagingft.*.so

# quick-sharun's OpenGL and Vulkan deployment copies every libEGL*/libGLX* and every ICD manifest
# of the build host: on a host with NVIDIA's driver, its user-space libraries (one exact driver
# version) and manifests went in, and the game loaded them next to the player's own driver
# (DLSS failed with NGX 0xbad00012; another driver version would not match the kernel module).
# NVIDIA's driver always comes from the host: launcher/bbport_vulkan.py points Vulkan at it.
find "$appdir" \( -iname '*nvidia*' \( -name '*.so*' -o -name '*.json' \) -o -name 'libcuda.so*' \
       -o -name 'libnvcuvid.so*' \) -print -exec rm -f {} +
# DEPLOY_PYTHON copies the build host's whole site-packages (scipy, Qt bindings, ... 431 MB on
# the build PC). The launcher imports only PyGObject (gi, with pycairo) and Pillow.
for site in "$appdir"/lib/python3*/site-packages; do
    find "$site" -mindepth 1 -maxdepth 1 ! -name gi ! -name cairo ! -name PIL \
        ! -name 'PyGObject-*.dist-info' ! -name 'pycairo-*.dist-info' ! -name 'pillow-*.dist-info' \
        -exec rm -rf {} +
done
# DLSS (NVIDIA RTX), when tools/build_dlss.sh has built the bridge: it and NVIDIA's library, copied
# after quick-sharun, which strips and patches every library in the AppDir. NVIDIA's DLSS library
# is signed: once changed, NGX refused it (0xbad00012) and DLSS was unavailable in the AppImage.
if [[ -f $root/out/libbbport_dlss.so ]]; then
    mkdir -p "$appdir/share/bbport/dlss"
    cp "$root"/out/libbbport_dlss.so "$root"/out/libnvidia-ngx-dlss.so.* \
        "$root"/out/NVIDIA-DLSS-LICENSE.txt "$appdir/share/bbport/dlss/"
fi
# Licenses of everything the package carries (MIT, BSD and zlib want their notices to go with the
# binaries): gzport's, the components compiled into it, and the Arch packages whose libraries and
# headers went in. share/bbport/licenses, and dist/...-LICENSES.txt with all of them in one file.
lic=$d/licenses
mkdir -p "$lic/components" "$lic/system"
cp "$root/LICENSE" "$lic/gzport-LICENSE.txt"
while read -r name file; do
    cp "$root/$file" "$lic/components/$name.txt"
done <<'LIST'
shadPS4 gpu/shadps4/LICENSE
FSR-Vulkan gpu/third_party/fsr-vulkan/LICENSE.txt
FSR-Vulkan-NOTICE gpu/third_party/fsr-vulkan/NOTICE.md
FSR-Vulkan-UPSTREAM gpu/third_party/fsr-vulkan/UPSTREAM.md
AMD-FidelityFX-SDK gpu/third_party/fsr-vulkan/upstream/ffx-1.1.4/sdk/LICENSE.txt
Dear-ImGui gpu/third_party/imgui/LICENSE.txt
LibAtrac9 third_party/LibAtrac9/LICENSE
sirit gpu/third_party/sirit/LICENSE.txt
SPIRV-Headers gpu/third_party/sirit/externals/SPIRV-Headers/LICENSE
half gpu/third_party/half/LICENSE.txt
cpp-httplib gpu/third_party/httplib/LICENSE
DejaVu-fonts gpu/third_party/fonts/LICENSE-DejaVu.txt
LIST
# Notices at the top of the sources themselves: AMD's GCN register headers, FSR 1, and AMD's FSR
# SDK 2.3 files in FSR-Vulkan (each carries this MIT notice).
for pair in AMD-GCN-headers:gpu/third_party/gcn/include/gcn/si_ci_vi_merged_offset.h \
            AMD-FSR1:gpu/shadps4/video_core/host_shaders/fsr/ffx_a.h \
            AMD-FSR-SDK-2.3:gpu/third_party/fsr-vulkan/upstream/ffx-2.3.0/Kits/FidelityFX/api/include/ffx_api_loader.h; do
    awk '/^[[:space:]]*($|\/\/|\/\*|\*)/ {print; next} {exit}' "$root/${pair#*:}" > "$lic/components/${pair%%:*}.txt"
done
if command -v pacman >/dev/null; then
    # The packages owning the libraries quick-sharun collected (lib/ mirrors /usr/lib), the
    # programs, and the header-only and static libraries the build compiled in.
    {
        find "$appdir/lib" -type f -name '*.so*' -printf '/usr/lib/%P\n' | while read -r f; do
            if [[ -e $f ]]; then echo "$f"; fi
        done | xargs -r pacman -Qqo 2>/dev/null || true
        pacman -Qqo "$(command -v python3)" "$(command -v vulkaninfo)" 2>/dev/null || true
        printf '%s\n' fmt magic_enum robin-map xxhash vulkan-memory-allocator boost zydis miniz \
            glslang spirv-cross spirv-headers xbyak protobuf nlohmann-json vulkan-headers
    } | sort -u > "$work/packages"
    printf '%s\n' 'Arch Linux packages whose libraries or headers are in this AppImage: name, version,' \
        'licenses. Their sources: https://gitlab.archlinux.org/archlinux/packaging/packages/<name>' '' \
        > "$lic/system/PACKAGES.txt"
    while read -r pkg; do
        pacman -Qi "$pkg" >/dev/null 2>&1 || continue
        licenses=$(LC_ALL=C pacman -Qi "$pkg" | sed -n 's/^Licenses *: //p')
        echo "$(pacman -Q "$pkg")  $licenses" >> "$lic/system/PACKAGES.txt"
        if [[ -d /usr/share/licenses/$pkg ]]; then cp -rL "/usr/share/licenses/$pkg" "$lic/system/"; fi
        # Licenses named by SPDX identifier only: their texts from the licenses package.
        for id in $(grep -oE '[A-Za-z0-9.+-]+' <<<"$licenses"); do
            if [[ -f /usr/share/licenses/spdx/$id.txt ]]; then
                mkdir -p "$lic/system/spdx"; cp "/usr/share/licenses/spdx/$id.txt" "$lic/system/spdx/"
            fi
        done
    done < "$work/packages"
fi
cat > "$lic/README.txt" <<'EOF'
GODZILLA for Linux (gzport) is free software under the GNU GPL v2 or later (gzport-LICENSE.txt).
Its complete source code: https://github.com/johnnygentoo/gzport (the tag of this release).

components/  the projects compiled into gzport, with their licenses and notices
system/      the Arch Linux packages whose libraries or headers this AppImage carries
             (PACKAGES.txt: name, version, licenses; the texts in their folders and in spdx/)

The AppImage runtime and sharun (github.com/VHSgunzo/uruntime, github.com/VHSgunzo/sharun, via
github.com/pkgforge-dev/Anylinux-AppImages) are under their own licenses.
No part of the game GODZILLA is included.
EOF
mkdir -p "$root/dist"
find "$lic" -type f | sort | while read -r f; do
    printf '\n==== %s ====\n\n' "${f#"$lic"/}"; cat "$f"
done > "$root/dist/GODZILLA-gzport-x86_64.AppImage-LICENSES.txt"
if [[ -n $net ]]; then
    module=$(find "$appdir/lib" -name libbbnet.so -print -quit)
    [[ -n $module ]] || { echo 'libbbnet.so is missing from the AppDir' >&2; exit 1; }
    mkdir -p "$d/net"
    ln -sf "$(realpath --relative-to="$d/net" "$module")" "$d/net/libbbnet.so"
fi
for driver in radeon intel; do
    ls "$appdir"/share/vulkan/icd.d/${driver}_icd*.json "$appdir"/lib/libvulkan_$driver.so \
        >/dev/null 2>&1 || { echo "Mesa's $driver Vulkan driver is missing from the AppDir" >&2; exit 1; }
done
# sharun points Vulkan at these (VK_DRIVER_FILES), plus the host's NVIDIA manifest when there is
# one, never at the host's Mesa.
"$quick" --make-appimage

mkdir -p "$root/dist"
mv -f "$work"/*.AppImage "$root/dist/GODZILLA-gzport-x86_64.AppImage"
ls -lh "$root/dist/GODZILLA-gzport-x86_64.AppImage"

# Legal notice

## You need your own copy of the game

gzport is source code only. It contains **no part of GODZILLA**: no executable, no game data,
no movies, music, voices, textures or fonts of the game, no saves, no keys and no PlayStation
system software. To use it you need:

- **your own copy of GODZILLA** for PlayStation 4 (North America, `CUSA02046`), with its 1.01
  update, **dumped by you from your own console**, and
- for add-ons (DLC), your own dumps of the add-ons you own.

Do not ask for game files, saves, keys or dumps in this project's issues, discussions or pull
requests, and do not post links to them. Such requests and links are removed.

## What this repository contains, and what it never will

The repository holds the port's own source code (GPL v2 or later), third-party open-source
components under their own licenses (see [README.md](README.md#credits) and
[BBPORT.md](BBPORT.md#credits-and-licenses)), documentation, and an original launcher icon drawn
for this project.

It never holds, and pull requests that add them are refused:

- files from the game or its updates and add-ons: `eboot.bin`, `sce_sys/`, `sce_module/`, `*.pac`,
  `*.at9`, `*.mp4`, `*.pkg`, `param.sfo`, trophy files, or anything extracted from them;
- saves, trophies or user folders (`user/`, `savedata/`);
- keys or credentials: the trophy key, shadNet accounts and passwords, server registration keys;
- PlayStation firmware or system libraries;
- AMD FSR 4 or NVIDIA DLSS libraries (the build makes them from files you provide).

The `.gitignore` keeps all of these out of commits. The libraries inside your dump (its
`sce_module` folder) are loaded from your dump when you play; they are never copied into the
repository.

## Not affiliated

gzport is an independent, non-commercial fan project. It is **not affiliated with, endorsed by or
sponsored by** Toho Co., Ltd., Bandai Namco Entertainment Inc., Natsume Atari Inc. or Sony
Interactive Entertainment LLC.

GODZILLA and the related characters are trademarks of Toho Co., Ltd. PlayStation and PS4 are
trademarks of Sony Interactive Entertainment Inc. NVIDIA and DLSS are trademarks of NVIDIA
Corporation; AMD and FidelityFX are trademarks of Advanced Micro Devices, Inc. All other
trademarks belong to their owners. They are used here only to say what the software works with.

## Online play

The versus mode works only between PCs running gzport, through a matchmaking server you run
yourself on your own network ([docs/LAN-VERSUS.md](docs/LAN-VERSUS.md)). gzport does not connect
to PlayStation Network and does not let you sign in to it.

## No warranty

gzport is free software under the GNU General Public License v2 or later ([LICENSE](LICENSE)). It
comes with **no warranty of any kind**, to the extent permitted by law. Keep backups of your
saves. Using it is at your own risk.

This notice explains the project's rules; it is not legal advice. The laws on dumping and backing
up your own games differ between countries: follow the ones that apply where you live.

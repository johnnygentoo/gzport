# Versus over the LAN

GODZILLA's online versus mode (VS MODE [FREE]) works between PCs running this port, through a
shadNet server of your own. Tested with two players on one home network (2026-10-18): random
search, both players ready, the match itself.

## How it works

The game finds the other players through PSN matchmaking (NpMatching2: rooms, room member data,
signaling) and sends the match over libSceRudp on a P2P socket (vport 778). Here:

- **Matchmaking:** the shadNet server ([shadnet-p2p](https://github.com/Wozzardman/shadnet-p2p))
  with [tools/shadnet-server/godzilla-versus.patch](../tools/shadnet-server/godzilla-versus.patch):
  each player's ready flag is room member data (`SetRoomMemberDataInternal`, attr 0x59, byte 0),
  and the game counts its own flag too, so the server sends room and member events to their
  sender as well. A player who backs out of the lobby is taken out of every room it was in.
- **The online module** (`gpu/bbnet`): the same request and its event (0x1107), the player's own
  address (`SignalingGetLocalNetInfo`), refusals as PSN error codes, and libSceRudp
  (`gpu/bbnet/rudp.cpp`; both players run it, so its wire format is its own).

## Setup

1. **The server**, on one always-on PC of the network. With Docker:
   [tools/shadnet-server](../tools/shadnet-server) (the patch is applied in the image), and
   [SERVER.md](SERVER.md) for the rest; `SHADNET_HOST` is the PC's LAN address. Without Docker,
   build shadnet-p2p (Qt 6.8 or newer with qt6-httpserver and qt6-websockets: on Arch
   `pacman -Syu qt6-httpserver qt6-websockets`), apply the patch, and in `shadnet.cfg` set
   `Host` to the LAN address, `Matching2Enabled=true`, `StatsEnabled=false` and a
   `RegistrationSecretKey`.
2. **Accounts**, one per player:
   `shadnet-sample <server> 31313 register <name> <password> <email> <secret key>`.
3. **Each PC** starts the game with:

   ```sh
   BB_ONLINE=1 BB_SHADNET_SERVER=<server>:31313 BB_SHADNET_WEBAPI=http://<server>:31315 \
   BB_SHADNET_NPID=<name> BB_SHADNET_PASSWORD=<password> BB_USER_NAME=<name> \
   BB_UPNP=0 SHADPS4_P2P_PORT=3658 bash run.sh
   ```

   (`BB_GAME_DIR` and `BB_CONFIG` as usual.) The P2P port (UDP 3658) must be open between the
   PCs; on one network nothing else is needed.

Then **Online → VS MODE → random search** on every PC: the first one creates the room, the
others join it, everyone confirms, and the match starts by itself.

## Debugging

`BB_NET_LOG=debug` logs the online module's classes only (network, PSN, Rudp, shadNet), without
the GPU library's debug output. The server's journal (`journalctl -t shadnet`) shows rooms,
joins and each player's ready data. `BB_RUDP_DROP=N` drops N% of Rudp datagrams (tests).

Not working yet: friend search (the friend list dialog is offline only).

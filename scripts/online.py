#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-2.0-or-later
"""GODZILLA's versus over the LAN (BB_ONLINE=1, docs/LAN-VERSUS.md): the game's online variables
for a shadNet server of the players' own, and the launcher's connection test of that server.

`online.py check --server HOST[:PORT]` tests the server's TCP port and its UDP port.
"""
import argparse
import os
from pathlib import Path
import re
import socket
import struct
import subprocess

# The shadNet server's UDP port (shadnet.cfg MatchingUdpPort): the game pings it to learn its public
# address, which the server hands to the other player of a match.
STUN_PORT = 31314
# The online ID of the connection test's ping: the server keeps one address per online ID, and the
# player's own would replace the address of a game running meanwhile.
STUN_TEST_ID = b'bbport-udp-test'


def stun_ping(host, port=STUN_PORT, timeout=2.0, attempts=3):
    """The public (address, port) the shadNet server sees for this computer, from the ping the
    game sends it (np_signaling_helpers.cpp: a 0xffff signaling header, command 1, the online ID
    and the local address); OSError, TimeoutError when nothing answers."""
    ping = b'\xff\xff\xff\xff' + b'\x01' + STUN_TEST_ID.ljust(16, b'\0') + bytes(4)
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        sock.settimeout(timeout)
        address = socket.gethostbyname(host)
        for _ in range(attempts):
            sock.sendto(ping, (address, port))
            try:
                reply, sender = sock.recvfrom(64)
            except TimeoutError:
                continue
            if sender[0] == address and len(reply) == 10 and reply[:4] == b'\xff' * 4:
                return socket.inet_ntoa(reply[4:8]), struct.unpack('!H', reply[8:10])[0]
        raise TimeoutError(f'no answer from {host}:{port} (UDP)')


# The P2P port the launcher suggests pinning (SHADPS4_P2P_PORT) and opening.
P2P_PORT = 3658


def active_firewalls(ufw_conf=Path('/etc/ufw/ufw.conf'), systemctl='/usr/bin/systemctl'):
    """Firewalls that drop unrequested incoming UDP by default, read without root: ufw when its
    configuration enables it, firewalld when its service runs. The host's systemctl runs without
    the AppImage's library paths."""
    found = []
    try:
        if re.search(r'^\s*ENABLED\s*=\s*yes', ufw_conf.read_text(errors='replace'), re.M):
            found.append('ufw')
    except OSError:
        pass
    try:
        env = {k: v for k, v in os.environ.items() if k not in ('LD_LIBRARY_PATH', 'LD_PRELOAD')}
        if subprocess.run([systemctl, 'is-active', '--quiet', 'firewalld'], env=env,
                          timeout=3).returncode == 0:
            found.append('firewalld')
    except (OSError, subprocess.SubprocessError):
        pass
    return found


def default_gateway(route=Path('/proc/net/route')):
    """The IPv4 default gateway (the router, which answers UPnP), or None."""
    try:
        for line in route.read_text().splitlines()[1:]:
            fields = line.split()
            if len(fields) > 2 and fields[1] == '00000000' and fields[2] != '00000000':
                return socket.inet_ntoa(int(fields[2], 16).to_bytes(4, 'little'))
    except (OSError, ValueError):
        pass
    return None


def firewall_commands(firewall, gateway=None, port=P2P_PORT):
    """(open the P2P port, let the router's UPnP replies in or None) for a firewall."""
    if firewall == 'ufw':
        return (f'sudo ufw allow {port}/udp',
                f'sudo ufw allow from {gateway} proto udp' if gateway else None)
    return (f'sudo firewall-cmd --permanent --add-port={port}/udp && sudo firewall-cmd --reload',
            None)


# shadNet's TCP protocol (gpu/bbnet/shadps4/shadnet/client.h): a 15-byte header (packet type u8,
# command u16, total size u32, packet id u64, little endian); the server greets with ServerInfo
# (its protocol version, u32) and answers Login with an error byte. srv.shadps4.net answers 8 for
# an unknown name as well as for a wrong password.
SHADNET_HEADER = struct.Struct('<BHIQ')
SHADNET_PROTOCOL = 1
LOGIN_ERRORS = {5: 'error', 6: 'already signed in', 7: 'no such account',
                8: 'wrong name or password', 9: 'wrong token'}


def proto_string(field, text):
    data = text.encode()
    length, varint = len(data), bytearray()
    while True:
        varint.append(length & 0x7f | (0x80 if length > 0x7f else 0))
        length >>= 7
        if not length:
            return bytes([field << 3 | 2]) + bytes(varint) + data


# A server's sign-in can take seconds: shadnet-p2p checks the password with a slow hash (about
# 7 s on a home server).
def shadnet_login(host, port, npid, password, timeout=20.0):
    """Signs in to a shadNet server as the game does and leaves at once: (ok, detail), detail an
    entry of LOGIN_ERRORS, 'protocol vN' or the socket error."""
    def receive(sock, size):
        data = b''
        while len(data) < size:
            chunk = sock.recv(size - len(data))
            if not chunk:
                raise ConnectionError('the server closed the connection')
            data += chunk
        return data

    def packet(sock):
        kind, command, total, _id = SHADNET_HEADER.unpack(receive(sock, SHADNET_HEADER.size))
        if not SHADNET_HEADER.size <= total <= 0x800000:
            raise ConnectionError('not a shadNet server')
        return kind, command, receive(sock, total - SHADNET_HEADER.size)

    with socket.create_connection((host, port), timeout=timeout) as sock:
        kind, _command, payload = packet(sock)
        if kind != 3:
            raise ConnectionError('not a shadNet server')
        version = struct.unpack_from('<I', payload)[0] if len(payload) >= 4 else SHADNET_PROTOCOL
        if version != SHADNET_PROTOCOL:
            return False, f'protocol v{version}'
        request = (proto_string(1, npid) + proto_string(2, password) +
                   proto_string(4, 'CUSA02046') + proto_string(5, 'GODZILLA'))
        body = struct.pack('<I', len(request)) + request
        sock.sendall(SHADNET_HEADER.pack(0, 0, SHADNET_HEADER.size + len(body), 1) + body)
        while True:  # notifications may come first
            kind, command, payload = packet(sock)
            if kind == 1 and command == 0:
                error = payload[0] if payload else 1
                return error == 0, LOGIN_ERRORS.get(error, f'code {error}') if error else ''


# GODZILLA's versus over the LAN (docs/LAN-VERSUS.md): a shadNet server of the players' own with
# tools/shadnet-server/godzilla-versus.patch, no community server, no UPnP. The game's P2P sockets
# go through this UDP port; pinned, so that it can be opened between the PCs.
LAN_P2P_PORT = 3658


def lan_server(settings):
    """The LAN server as host:port (shadNet's 31313 when no port is given), '' when unset."""
    server = str(settings.get('online_server') or '').strip()
    if server and ':' not in server:
        server += ':31313'
    return server


def lan_environment(settings):
    """The game's online variables for GODZILLA's LAN versus. The online ID is also the name the
    game shows for the player (BB_USER_NAME)."""
    server = lan_server(settings)
    host = server.rsplit(':', 1)[0]
    npid = str(settings.get('online_npid') or '').strip()
    port = int(settings.get('online_p2p_port') or LAN_P2P_PORT)
    env = {
        'BB_ONLINE': '1',
        'BB_SHADNET_SERVER': server,
        'BB_SHADNET_WEBAPI': f'http://{host}:31315',
        'BB_SHADNET_NPID': npid,
        'BB_SHADNET_PASSWORD': settings.get('online_password') or '',
        'BB_UPNP': '0',
        'SHADPS4_P2P_PORT': str(port if 0 < port < 65536 else LAN_P2P_PORT),
    }
    if npid:
        env['BB_USER_NAME'] = npid
    return env


def lan_check(server, account=None):
    """(name, address, ok, detail) for the LAN server: its TCP port ('shadnet'), its UDP port
    ('stun', detail: this PC's address as the server sees it, or 'timeout') and, with account
    (npid, password), the sign-in ('login', detail: an entry of LOGIN_ERRORS, 'protocol vN' or why it could not be
    tried)."""
    results = []
    host, _sep, port = server.rpartition(':')
    host = host or server
    try:
        socket.create_connection((host, int(port or 31313)), timeout=4).close()
        results.append(('shadnet', server, True, ''))
    except (OSError, ValueError) as error:
        results.append(('shadnet', server, False, str(error)))
    try:
        public, public_port = stun_ping(host)
        results.append(('stun', f'{host}:{STUN_PORT}', True, f'{public}:{public_port}'))
    except TimeoutError:
        results.append(('stun', f'{host}:{STUN_PORT}', False, 'timeout'))
    except OSError as error:
        results.append(('stun', f'{host}:{STUN_PORT}', False, str(error)))
    npid, password = account or ('', '')
    if npid and password and results[0][2]:
        try:
            ok, detail = shadnet_login(host, int(port or 31313), npid, password)
            results.append(('login', npid, ok, detail))
        except (OSError, ValueError) as error:
            results.append(('login', npid, False, str(error)))
    return results


def main():
    parser = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    sub = parser.add_subparsers(dest='command', required=True)
    check = sub.add_parser('check')
    check.add_argument('--server', default=os.environ.get('BB_SHADNET_SERVER', ''))
    a = parser.parse_args()
    server = lan_server({'online_server': a.server})
    if not server:
        parser.error('no server: --server HOST[:PORT] or BB_SHADNET_SERVER')
    for name, address, ok, detail in lan_check(server):
        print(f'{name}: {address}: {"reachable" if ok else "not reachable"} {detail}'.rstrip())


if __name__ == '__main__':
    main()

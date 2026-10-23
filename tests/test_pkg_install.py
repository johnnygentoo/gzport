from paths import ROOT
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

import pkg_install
from test_game_check import param_sfo

# A stand-in for pkgextract: a "package" is the PKG header (magic, content ID) and, after it, a
# JSON list of its files; it refuses an output folder that exists, as pkgextract without -f does.
FAKE_EXTRACTOR = '''import json, sys
from pathlib import Path
args = sys.argv[1:]
out, pkg = Path(args[args.index('-o') + 1]), Path(args[-1])
if out.exists():
    sys.exit('output directory already exists')
for name, data in json.loads(pkg.read_bytes()[0x80:]).items():
    (out / name).parent.mkdir(parents=True, exist_ok=True)
    (out / name).write_bytes(bytes.fromhex(data))
'''


def package(path, content_id, category, version, files):
    header = bytearray(0x80)
    header[:4] = b'\x7fCNT'
    header[0x40:0x40 + len(content_id)] = content_id.encode()
    files = {'sce_sys/param.sfo': param_sfo({'CATEGORY': category, 'APP_VER': version,
                                             'TITLE_ID': content_id[7:16]}), **files}
    path.write_bytes(bytes(header) + json.dumps({k: v.hex() for k, v in files.items()}).encode())
    return path


class PkgInstallTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.extractor = self.root / 'pkgextract'
        self.extractor.write_text(f'#!{sys.executable}\n' + FAKE_EXTRACTOR)
        self.extractor.chmod(0o755)
        self.dest = self.root / 'games'
        self.lines = []
        checked = mock.patch.object(pkg_install, 'problem', return_value=None)
        checked.start()
        self.addCleanup(checked.stop)

    def tearDown(self):
        self.tmp.cleanup()

    def install(self, *pkgs):
        return pkg_install.install(pkgs, self.dest, str(self.extractor), self.lines.append)

    def test_game_updates_oldest_first_and_add_ons_apart(self):
        game = package(self.root / 'a.pkg', 'UP0700-CUSA02046_00-PS4GODZILLA00000', 'gd', '01.00',
                       {'eboot.bin': b'1.00', 'dvdroot_ps4/kept.bin': b'base'})
        late = package(self.root / 'b.pkg', 'UP0700-CUSA02046_00-PS4GODZILLA00000', 'gp', '01.02',
                       {'eboot.bin': b'1.02'})
        early = package(self.root / 'c.pkg', 'UP0700-CUSA02046_00-PS4GODZILLA00000', 'gp', '01.01',
                        {'eboot.bin': b'1.01', 'dvdroot_ps4/new.bin': b'1.01'})
        dlc = package(self.root / 'd.pkg', 'UP0700-CUSA02046_00-GODZILLADLC00001', 'ac', '01.00', {})
        game_dir, dlc_dir = self.install(late, dlc, game, early)
        self.assertEqual(game_dir, self.dest.resolve() / 'CUSA02046')
        self.assertEqual((game_dir / 'eboot.bin').read_bytes(), b'1.02')
        self.assertEqual((game_dir / 'dvdroot_ps4/kept.bin').read_bytes(), b'base')
        self.assertEqual((game_dir / 'dvdroot_ps4/new.bin').read_bytes(), b'1.01')
        self.assertEqual(dlc_dir, self.dest.resolve() / 'DLC')
        self.assertTrue((dlc_dir / 'GODZILLADLC00001/sce_sys/param.sfo').is_file())
        self.assertEqual(sorted(p.name for p in self.dest.iterdir()), ['CUSA02046', 'DLC'])
        self.assertIn('Install: the game is ready (GODZILLA 1.01)', self.lines)

    def test_an_existing_game_folder_is_never_replaced(self):
        game = package(self.root / 'a.pkg', 'UP0700-CUSA02046_00-PS4GODZILLA00000', 'gd', '01.00',
                       {'eboot.bin': b'new'})
        (self.dest / 'CUSA02046').mkdir(parents=True)
        (self.dest / 'CUSA02046/eboot.bin').write_bytes(b'mine')
        with self.assertRaisesRegex(pkg_install.InstallError, 'already exists'):
            self.install(game)
        self.assertEqual((self.dest / 'CUSA02046/eboot.bin').read_bytes(), b'mine')
        self.assertEqual([p.name for p in self.dest.iterdir()], ['CUSA02046'])

    def test_not_a_package_or_two_titles_or_no_game(self):
        other = self.root / 'notes.pkg'
        other.write_bytes(b'not a package' * 20)
        with self.assertRaisesRegex(pkg_install.InstallError, 'not a PS4 package'):
            self.install(other)
        us = package(self.root / 'a.pkg', 'UP0700-CUSA02046_00-PS4GODZILLA00000', 'gd', '01.00', {})
        eu = package(self.root / 'b.pkg', 'EP0000-CUSA99999_00-OTHERGAME0000000', 'gp', '01.00', {})
        with self.assertRaisesRegex(pkg_install.InstallError, 'different titles'):
            self.install(us, eu)
        update = package(self.root / 'c.pkg', 'UP0700-CUSA02046_00-PS4GODZILLA00000', 'gp', '01.01', {})
        with self.assertRaisesRegex(pkg_install.InstallError, '0 game packages'):
            self.install(update)
        self.assertFalse((self.dest / 'CUSA02046').exists())
        self.assertEqual([p.name for p in self.dest.iterdir()], [])   # no work folder left


if __name__ == '__main__':
    unittest.main()

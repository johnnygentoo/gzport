"""The repository never holds game files, saves or keys (LEGAL.md): every tracked file is checked
by name and by content, so a commit that adds one fails the tests."""
from paths import ROOT
import re
import subprocess
import unittest

# Names of PS4 game content, saves, keys and personal settings.
FORBIDDEN_NAMES = re.compile(
    r'(^|/)(eboot\.bin|param\.sfo|DATA\.BIN|icon0\.png|keystone|npbind\.dat|nptitle\.dat|'
    r'accounts\.txt|registration\.key|bbport\.ini|settings\.json|\.env)$'
    r'|\.(elf|self|prx|sprx|sfo|trp|pac|at9|mp4|pkg|dcx|tpf|gfx|dds|key|pem|p12)$'
    r'|(^|/)(sce_sys|sce_module|savedata|SAVEDATA\d+|CUSA\d{5}[^/]*)/', re.IGNORECASE)
# Content of PS4 files whatever their name: signed executable (SELF), PKG, param.sfo, PFS image.
MAGICS = {b'\x4f\x15\x3d\x1d': 'PS4 signed executable (SELF)', b'\x7fCNT': 'PS4 package (PKG)',
          b'\x00PSF': 'PS4 param.sfo', b'\x7fFIH': 'PS4 file image'}
# Tracked files that legitimately match a rule above.
ALLOWED = set()
# Anything this large is not source code; a game archive or movie would be.
MAX_BYTES = 4 * 1024 * 1024


def tracked_files():
    try:
        out = subprocess.run(['git', '-C', str(ROOT), 'ls-files', '-z'], capture_output=True,
                             check=True).stdout
    except (OSError, subprocess.CalledProcessError):
        return None
    return [name for name in out.decode('utf-8', 'replace').split('\0') if name]


class NoGameFilesTests(unittest.TestCase):
    def setUp(self):
        self.files = tracked_files()
        if self.files is None:
            self.skipTest('not a git checkout')

    def test_no_game_or_personal_file_names(self):
        found = [f for f in self.files if FORBIDDEN_NAMES.search(f) and f not in ALLOWED]
        self.assertEqual(found, [], 'game files, saves, keys or settings are tracked (LEGAL.md)')

    def test_no_ps4_file_contents(self):
        found = []
        for name in self.files:
            path = ROOT / name
            if not path.is_file() or path.is_symlink():
                continue
            with open(path, 'rb') as f:
                head = f.read(4)
            if head in MAGICS:
                found.append(f'{name}: {MAGICS[head]}')
        self.assertEqual(found, [], 'PS4 game content is tracked (LEGAL.md)')

    def test_no_large_files(self):
        found = [f'{name}: {(ROOT / name).stat().st_size} bytes' for name in self.files
                 if (ROOT / name).is_file() and (ROOT / name).stat().st_size > MAX_BYTES]
        self.assertEqual(found, [], 'a tracked file is larger than source code ever is')

    def test_rules_catch_game_files(self):
        for name in ('CUSA02046/eboot.bin', 'game/sce_sys/param.sfo', 'x/voice_001.at9',
                     'user/savedata/1/CUSA02046/SAVEDATA00/DATA.BIN', 'ch03.mp4', 'a/b.pac',
                     'sce_module/libc.prx', 'data/accounts.txt', 'bbport.ini', 'UP0700.pkg',
                     'menu/atlas.dds', 'menu/common.tpf', 'menu/gesturetop.gfx'):
            self.assertTrue(FORBIDDEN_NAMES.search(name), name)
        for name in ('src/runtime_ngs2.c', 'launcher/godzilla.svg', 'docs/LAN-VERSUS.md',
                     'tools/shadnet-server/godzilla-versus.patch', 'patches/Godzilla.xml'):
            self.assertFalse(FORBIDDEN_NAMES.search(name), name)


if __name__ == '__main__':
    unittest.main()

#!/usr/bin/env bash
# Copies this PC's GODZILLA save to other PCs running gzport, over ssh, so every player starts
# from the same progress. Each PC's own save is moved to user/savedata-backups first.
#
#   scripts/push-save.sh user@host[:/path/to/Godzillaport] ...
#
# The path defaults to this checkout's path. BB_USER_DIR picks this PC's user folder as in
# run.sh; the other PCs' saves are in their checkout's user/ folder.
set -euo pipefail

here=$(cd "$(dirname "$0")/.." && pwd)
saves=${BB_USER_DIR:-$here/user}/savedata/1/CUSA02046

if (($# == 0)); then
    echo "usage: $0 user@host[:/path/to/Godzillaport] ..." >&2
    exit 2
fi
if [[ ! -f $saves/SAVEDATA00/DATA.BIN ]]; then
    echo "No save here: $saves/SAVEDATA00/DATA.BIN" >&2
    exit 1
fi
if pgrep -x bb-probe > /dev/null; then
    echo "Note: the game is running here; the copy is the save as it was last written." >&2
fi

failed=0
for target in "$@"; do
    host=${target%%:*}
    dir=$here
    [[ $target == *:* ]] && dir=${target#*:}
    echo "== $host ($dir)"
    # The remote side refuses while the game runs there (it would write its own save over this
    # one), then moves the old save aside.
    if ! ssh -o ConnectTimeout=5 "$host" bash -s -- "$dir" << 'EOF'
set -e
dir=$1
if pgrep -x bb-probe > /dev/null; then
    echo "  the game is running there; close it first" >&2
    exit 1
fi
[[ -d $dir ]] || { echo "  no $dir there" >&2; exit 1; }
saves=$dir/user/savedata/1/CUSA02046
if [[ -d $saves ]]; then
    backup=$dir/user/savedata-backups/CUSA02046-$(date +%Y%m%d-%H%M%S)
    mkdir -p "${backup%/*}"
    mv "$saves" "$backup"
    echo "  their save: $backup"
fi
mkdir -p "$saves"
EOF
    then
        failed=1
        continue
    fi
    if rsync -a "$saves/" "$host:$dir/user/savedata/1/CUSA02046/"; then
        echo "  copied"
    else
        failed=1
    fi
done
exit $failed

#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
if [ "$(uname -s)" != Darwin ]; then echo 'Run this installer on your Mac.'; exit 1; fi
echo 'First stop your old Terminal launcher with Control-C.'
echo 'Select your EXISTING installed Sales-Command folder, not this download.'
TARGET_APP="$(osascript -e 'POSIX path of (choose folder with prompt "Choose your EXISTING installed Sales-Command folder (with your speech model)")')"
if [ ! -x "$TARGET_APP/tools/.venv/bin/python" ]; then
  echo 'That folder does not contain the installed speech helper. Run this installer again and choose the original Sales-Command folder you already use.'
  exit 1
fi
"$TARGET_APP/tools/.venv/bin/python" tools/install-mac-icon.py --root "$TARGET_APP"

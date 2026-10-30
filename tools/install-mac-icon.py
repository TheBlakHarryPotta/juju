#!/usr/bin/env python3
"""Build a stay-open macOS applet using Apple's built-in compiler."""
import argparse
from pathlib import Path
import plistlib
import shutil
import subprocess
import sys
import tempfile


def install(source, root, applications):
    root = root.resolve()
    if not (root / 'dist/index.html').is_file() or not (root / 'tools/.venv/bin/python').is_file():
        raise ValueError('Select your existing installed Sales-Command folder, containing dist and tools/.venv. No model download is needed.')
    destination = applications / 'Sales Command.app'
    if destination.exists():
        raise ValueError('Sales Command.app already exists in your Applications folder. Quit it and move that launcher to Trash before installing a replacement. Your Sales-Command data folder should stay where it is.')
    applications.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix='.sales-command-icon-', dir=applications) as temporary:
        bundle = Path(temporary) / 'Sales Command.app'
        subprocess.run(['/usr/bin/osacompile', '-s', '-o', str(bundle), str(source / 'mac-launcher.applescript')], check=True)
        resources = bundle / 'Contents/Resources'
        (resources / 'installed-root.txt').write_text(str(root), encoding='utf-8')
        shutil.copy2(source / 'sales-command.icns', resources / 'sales-command.icns')
        plist_path = bundle / 'Contents/Info.plist'
        with plist_path.open('rb') as file:
            info = plistlib.load(file)
        info.update(CFBundleIdentifier='local.salescommand.launcher', CFBundleName='Sales Command',
                    CFBundleDisplayName='Sales Command', CFBundleIconFile='sales-command.icns',
                    CFBundleShortVersionString='1.0', CFBundleVersion='1', NSHighResolutionCapable=True)
        with plist_path.open('wb') as file:
            plistlib.dump(info, file)
        # No network download or speech changes. Copy only the versioned launcher helper.
        helper = root / 'tools/mac-launcher.py'
        if (source / 'mac-launcher.py').resolve() != helper.resolve():
            staged = helper.with_suffix('.py.new')
            shutil.copy2(source / 'mac-launcher.py', staged)
            staged.replace(helper)
        # osacompile's resource signature is invalidated by the icon/config changes.
        # Apply a local ad-hoc signature, with no developer-account or network dependency.
        subprocess.run(['/usr/bin/codesign', '--force', '--sign', '-', str(bundle)], check=True)
        subprocess.run(['/usr/bin/codesign', '--verify', '--strict', str(bundle)], check=True)
        bundle.rename(destination)
    subprocess.run(['/usr/bin/open', '-R', str(destination)], check=True)
    print('Installed:', destination)
    print('Double-click Sales Command to open Safari and start both local services.')
    print('Drag the app into your Dock. Quit Sales Command from the Dock to stop both services.')
    return destination


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', required=True, type=Path)
    args = parser.parse_args()
    if sys.platform != 'darwin':
        raise SystemExit('This installer runs on your Mac, not in the cloud workspace.')
    try:
        install(Path(__file__).resolve().parent, args.root, Path.home() / 'Applications')
    except (OSError, ValueError, subprocess.CalledProcessError) as error:
        raise SystemExit(str(error))


if __name__ == '__main__':
    main()

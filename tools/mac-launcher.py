#!/usr/bin/env python3
"""Local-only service supervisor for the Sales Command macOS Dock app."""
import argparse
import fcntl
import hashlib
import json
import os
from pathlib import Path
import secrets
import signal
import socket
import subprocess
import sys
import time
import urllib.request


def socket_path(root):
    digest = hashlib.sha256(os.fsencode(root)).hexdigest()[:20]
    return f'/tmp/sc-{os.getuid()}-{digest}.sock'


def request(root, command, instance=''):
    with socket.socket(socket.AF_UNIX) as client:
        client.settimeout(2)
        client.connect(socket_path(root))
        client.sendall(json.dumps({'command': command, 'instance': instance}).encode() + b'\n')
        return json.loads(client.recv(4096))


def stop_children(children):
    # Only processes created by this supervisor are signalled; never kill by port/PID file.
    for child in children:
        try:
            # A speech engine child can outlive its helper process.
            os.killpg(child.pid, signal.SIGTERM)
        except ProcessLookupError:
            pass
    deadline = time.monotonic() + 8
    for child in children:
        try:
            child.wait(timeout=max(0.01, deadline - time.monotonic()))
        except subprocess.TimeoutExpired:
            pass
    for child in children:
        try:
            os.killpg(child.pid, signal.SIGKILL)
        except ProcessLookupError:
            pass
        child.wait()


def serve(root, app_port=4173, speech_port=8766):
    local = root / '.local'
    local.mkdir(mode=0o700, exist_ok=True)
    with (local / 'mac-launcher.lock').open('a') as lock:
        try:
            fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            return
        for port in (app_port, speech_port):
            with socket.socket() as check:
                try:
                    check.bind(('127.0.0.1', port))
                except OSError:
                    raise RuntimeError('A local port is already in use. Stop the old Terminal launcher with Control-C, then click Sales Command again.')
        path = socket_path(root)
        try:
            os.unlink(path)
        except FileNotFoundError:
            pass
        children = []
        logs = []
        running = True
        instance = secrets.token_hex(24)

        def shutdown(*_):
            nonlocal running
            running = False

        signal.signal(signal.SIGTERM, shutdown)
        signal.signal(signal.SIGINT, shutdown)
        try:
            for name, args in (
                ('app', [sys.executable, '-m', 'http.server', str(app_port), '--bind', '127.0.0.1', '--directory', str(root / 'dist')]),
                ('speech', [sys.executable, str(root / 'tools/speech_server.py'), '--port', str(speech_port)]),
            ):
                log = (local / f'{name}.log').open('ab', buffering=0)
                logs.append(log)
                children.append(subprocess.Popen(args, cwd=root, stdin=subprocess.DEVNULL,
                                                 stdout=log, stderr=log, start_new_session=True))
            # Do not send localhost traffic through a configured Internet proxy.
            opener = urllib.request.build_opener(urllib.request.ProxyHandler({}))
            deadline = time.monotonic() + 30
            while running:
                if any(child.poll() is not None for child in children):
                    raise RuntimeError('A service exited. Check .local/app.log and .local/speech.log in your installed app folder.')
                try:
                    with opener.open(f'http://127.0.0.1:{app_port}/', timeout=0.5) as response:
                        if response.status != 200:
                            raise OSError('App is not ready')
                    token = (root / 'tools/.speech-token').read_text().strip()
                    health = urllib.request.Request(f'http://127.0.0.1:{speech_port}/health', headers={
                        'Origin': f'http://127.0.0.1:{app_port}', 'X-Sales-Command-Token': token})
                    with opener.open(health, timeout=0.5) as response:
                        result = json.load(response)
                        if not result.get('ready'):
                            raise RuntimeError(result.get('message', 'Local transcription is not ready.'))
                    if any(child.poll() is not None for child in children):
                        raise RuntimeError('A service could not bind its port. Stop any earlier launcher and try again.')
                    break
                except (OSError, ValueError):
                    if time.monotonic() >= deadline:
                        raise RuntimeError('Local services did not become ready. Check .local logs in your installed folder.')
                    time.sleep(0.15)
            if not running:
                return
            with socket.socket(socket.AF_UNIX) as server:
                server.bind(path)
                os.chmod(path, 0o600)
                server.listen(4)
                server.settimeout(0.5)
                while running:
                    if any(child.poll() is not None for child in children):
                        raise RuntimeError('A local service stopped. Check .local logs, then reopen Sales Command.')
                    try:
                        client, _ = server.accept()
                    except socket.timeout:
                        continue
                    with client:
                        client.settimeout(1)
                        try:
                            data = json.loads(client.recv(4096))
                            if data.get('command') == 'stop' and secrets.compare_digest(data.get('instance', ''), instance):
                                running = False
                            client.sendall(json.dumps({'instance': instance, 'running': running}).encode())
                        except (OSError, ValueError, TypeError):
                            pass
        finally:
            stop_children(children)
            for log in logs:
                log.close()
            try:
                os.unlink(path)
            except FileNotFoundError:
                pass


def start(root):
    try:
        result = request(root, 'status')
        if result['running']:
            return result['instance']
    except (OSError, ValueError, KeyError):
        pass
    if not (root / 'dist/index.html').is_file() or not (root / 'tools/.venv/bin/python').is_file():
        raise RuntimeError('Choose your installed Sales-Command folder with dist and tools/.venv. Run setup-mac.command first if this is a new installation.')
    local = root / '.local'
    local.mkdir(mode=0o700, exist_ok=True)
    with (local / 'launcher.log').open('ab', buffering=0) as log:
        process = subprocess.Popen([sys.executable, str(Path(__file__).resolve()), 'serve', '--root', str(root)],
                                   cwd=root, stdin=subprocess.DEVNULL, stdout=log, stderr=log, start_new_session=True)
    deadline = time.monotonic() + 35
    while time.monotonic() < deadline:
        try:
            result = request(root, 'status')
            if result['running']:
                return result['instance']
        except (OSError, ValueError, KeyError):
            pass
        if process.poll() is not None:
            # Concurrent app launches may briefly overlap. Recheck the owning supervisor.
            time.sleep(0.2)
            try:
                return request(root, 'status')['instance']
            except (OSError, ValueError, KeyError):
                raise RuntimeError('Could not start both services. Stop any old Terminal launcher with Control-C. If it still fails, see .local/launcher.log in the installed folder.')
        time.sleep(0.15)
    process.terminate()
    try:
        process.wait(timeout=10)
    except subprocess.TimeoutExpired:
        process.kill()
        process.wait()
    raise RuntimeError('Startup timed out. See .local/launcher.log in your installed folder.')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command', choices=['start', 'serve', 'stop', 'status'])
    parser.add_argument('--root', required=True, type=Path)
    parser.add_argument('--instance', default='')
    args = parser.parse_args()
    root = args.root.resolve()
    try:
        if args.command == 'serve':
            serve(root)
        elif args.command == 'start':
            print(start(root))
        else:
            result = request(root, args.command, args.instance)
            if args.command == 'status' and (not result['running'] or result['instance'] != args.instance):
                raise RuntimeError('The local services have stopped. Quit and reopen Sales Command. See .local logs if it happens again.')
            if args.command == 'stop' and result['instance'] == args.instance:
                deadline = time.monotonic() + 10
                while time.monotonic() < deadline:
                    try:
                        if request(root, 'status')['instance'] != args.instance:
                            break
                    except (OSError, ValueError):
                        break
                    time.sleep(0.1)
    except (OSError, RuntimeError) as error:
        raise SystemExit(str(error))


if __name__ == '__main__':
    main()

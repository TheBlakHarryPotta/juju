#!/usr/bin/env python3
"""Lifecycle checks use disposable HTTP/speech fixtures, never the user's services."""
import importlib.util
import json
import os
from pathlib import Path
import socket
import subprocess
import sys
import tempfile
import time
import unittest
from unittest.mock import patch

TOOLS = Path(__file__).resolve().parents[1] / 'tools'


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


launcher = load('launcher', TOOLS / 'mac-launcher.py')
installer = load('installer', TOOLS / 'install-mac-icon.py')


def port():
    with socket.socket() as sock:
        sock.bind(('127.0.0.1', 0))
        return sock.getsockname()[1]


class Lifecycle(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix='sc icon space-')
        self.root = Path(self.temp.name)
        (self.root / 'dist').mkdir()
        (self.root / 'dist/index.html').write_text('fixture app')
        (self.root / 'tools/.venv/bin').mkdir(parents=True)
        (self.root / 'tools/.venv/bin/python').symlink_to(sys.executable)
        (self.root / 'tools/.speech-token').write_text('fixture-token')
        (self.root / 'tools/speech_server.py').write_text('''
from http.server import BaseHTTPRequestHandler,HTTPServer
import argparse,json
p=argparse.ArgumentParser();p.add_argument('--port',type=int);a=p.parse_args()
class H(BaseHTTPRequestHandler):
 def do_GET(self):
  ok=self.path=='/health' and self.headers.get('X-Sales-Command-Token')=='fixture-token' and self.headers.get('Origin','').startswith('http://127.0.0.1:')
  self.send_response(200 if ok else 403);self.end_headers();self.wfile.write(json.dumps({'ready':True}).encode())
HTTPServer(('127.0.0.1',a.port),H).serve_forever()
''')
        self.app_port, self.speech_port = port(), port()
        while self.speech_port == self.app_port:
            self.speech_port = port()
        self.process = None

    def spawn(self):
        script = 'import importlib.util,sys;from pathlib import Path;s=importlib.util.spec_from_file_location("m",sys.argv[1]);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);m.serve(Path(sys.argv[2]),int(sys.argv[3]),int(sys.argv[4]))'
        self.process = subprocess.Popen([sys.executable, '-c', script, str(TOOLS / 'mac-launcher.py'), str(self.root), str(self.app_port), str(self.speech_port)], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    def ready(self):
        deadline = time.monotonic() + 6
        while time.monotonic() < deadline:
            try:
                return launcher.request(self.root, 'status')
            except OSError:
                if self.process.poll() is not None:
                    self.fail(self.process.communicate()[1].decode())
                time.sleep(.05)
        self.fail('Fixture startup timed out')

    def assert_ports_free(self):
        for number in (self.app_port, self.speech_port):
            with socket.socket() as sock:
                self.assertNotEqual(sock.connect_ex(('127.0.0.1', number)), 0)

    def tearDown(self):
        if self.process:
            if self.process.poll() is None:
                self.process.terminate()
            self.process.communicate(timeout=12)
        self.temp.cleanup()

    def test_start_ready_reuse_wrong_instance_and_quit(self):
        self.spawn()
        info = self.ready()
        self.assertTrue(info['running'])
        # Repeated clicks adopt the same owner, without starting two copies.
        self.assertEqual(launcher.start(self.root), info['instance'])
        self.assertTrue(launcher.request(self.root, 'stop', 'wrong-instance')['running'])
        self.assertEqual(os.stat(launcher.socket_path(self.root)).st_mode & 0o777, 0o600)
        self.assertFalse(launcher.request(self.root, 'stop', info['instance'])['running'])
        self.process.communicate(timeout=12)
        self.assertEqual(self.process.returncode, 0)
        self.assert_ports_free()
        self.assertFalse(Path(launcher.socket_path(self.root)).exists())

    def test_conflicting_service_is_never_killed(self):
        with socket.socket() as unrelated:
            unrelated.bind(('127.0.0.1', self.app_port))
            unrelated.listen()
            self.spawn()
            _, error = self.process.communicate(timeout=4)
            self.assertNotEqual(self.process.returncode, 0)
            self.assertIn(b'already in use', error)
            self.assertGreater(unrelated.fileno(), 0)
            with socket.socket() as check:
                self.assertEqual(check.connect_ex(('127.0.0.1', self.app_port)), 0)

    def test_failed_speech_start_cleans_up_website(self):
        (self.root / 'tools/speech_server.py').write_text('raise SystemExit(3)')
        self.spawn()
        _, error = self.process.communicate(timeout=6)
        self.assertNotEqual(self.process.returncode, 0)
        self.assertIn(b'service exited', error)
        self.assert_ports_free()

    def test_termination_cleans_up_both_services(self):
        self.spawn()
        self.ready()
        self.process.terminate()
        self.process.communicate(timeout=12)
        self.assert_ports_free()

    def test_crashed_helper_cleans_up_its_term_resistant_descendant(self):
        child_port = port()
        while child_port in (self.app_port, self.speech_port):
            child_port = port()
        child_script = self.root / 'child.py'
        child_script.write_text('import socket,signal,time,sys;from pathlib import Path;signal.signal(signal.SIGTERM,signal.SIG_IGN);s=socket.socket();s.bind(("127.0.0.1",int(sys.argv[1])));s.listen();Path(sys.argv[2]).write_text("ready");time.sleep(60)')
        marker = self.root / 'child-ready'
        (self.root / 'tools/speech_server.py').write_text(
            'import subprocess,sys,time;from pathlib import Path\n'
            f'subprocess.Popen([sys.executable,{str(child_script)!r},{str(child_port)!r},{str(marker)!r}])\n'
            f'while not Path({str(marker)!r}).exists(): time.sleep(.02)\n'
            'raise SystemExit(3)\n')
        self.spawn()
        self.process.communicate(timeout=6)
        self.assertNotEqual(self.process.returncode, 0)
        self.assertTrue(marker.exists())
        with socket.socket() as check:
            self.assertNotEqual(check.connect_ex(('127.0.0.1', child_port)), 0)
        self.assert_ports_free()

    def test_installer_builds_and_signs_without_touching_model_or_token(self):
        import plistlib
        model = self.root / 'tools/model.bin'
        model.write_bytes(b'preserved-model')
        token = (self.root / 'tools/.speech-token').read_bytes()
        applications = self.root / 'Applications'
        commands = []

        def fake_run(args, **kwargs):
            commands.append(args)
            if args[0] == '/usr/bin/osacompile':
                bundle = Path(args[args.index('-o') + 1])
                (bundle / 'Contents/Resources').mkdir(parents=True)
                with (bundle / 'Contents/Info.plist').open('wb') as file:
                    plistlib.dump({'CFBundleExecutable': 'applet'}, file)

        with patch.object(installer.subprocess, 'run', side_effect=fake_run):
            app = installer.install(TOOLS, self.root, applications)
        self.assertEqual((app / 'Contents/Resources/installed-root.txt').read_text(), str(self.root))
        self.assertEqual((self.root / 'tools/mac-launcher.py').read_bytes(), (TOOLS / 'mac-launcher.py').read_bytes())
        self.assertEqual(model.read_bytes(), b'preserved-model')
        self.assertEqual((self.root / 'tools/.speech-token').read_bytes(), token)
        self.assertEqual([c[0] for c in commands], ['/usr/bin/osacompile', '/usr/bin/codesign', '/usr/bin/codesign', '/usr/bin/open'])
        with self.assertRaisesRegex(ValueError, 'already exists'):
            installer.install(TOOLS, self.root, applications)


if __name__ == '__main__':
    unittest.main(verbosity=2)

"""Minimal HTTP health server for Render Web Service hosting.

Runs alongside the existing Telegram polling bot without changing bot logic.
"""

import os
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from threading import Thread


class HealthHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path in ("/", "/health", "/healthz"):
            body = b"OK"
            self.send_response(200)
            self.send_header("Content-Type", "text/plain; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
            return

        self.send_response(404)
        self.end_headers()

    def log_message(self, format, *args):
        return


def start_keepalive() -> None:
    """Start the health server in a daemon thread."""
    port = int(os.getenv("PORT", "10000"))
    server = ThreadingHTTPServer(("0.0.0.0", port), HealthHandler)
    thread = Thread(target=server.serve_forever, daemon=True)
    thread.start()
    print(f"🌐 Render health server listening on 0.0.0.0:{port}", flush=True)

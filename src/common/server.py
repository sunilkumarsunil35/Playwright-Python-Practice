"""The practice web app every exercise runs against.

It serves the pages in site/ plus a small JSON API, all on localhost, so the tests never depend on
the internet. Run it on its own to click around in a real browser:

    python -m common.server          (from the src/ folder)
"""

import json
import threading
from http import HTTPStatus
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlparse

SITE_DIR = Path(__file__).resolve().parents[2] / "site"

USERS = {"tom": "secret", "ana": "hunter2"}
SESSION_PREFIX = "session-"

PRODUCTS = [
    {"id": 1, "name": "Laptop", "price": 999},
    {"id": 2, "name": "Keyboard", "price": 49},
    {"id": 3, "name": "Mouse", "price": 25},
    {"id": 4, "name": "Monitor", "price": 199},
]

PEOPLE = [
    {"id": 1, "name": "Leanne Graham", "email": "leanne@example.com"},
    {"id": 2, "name": "Ervin Howell", "email": "ervin@example.com"},
    {"id": 3, "name": "Clementine Bauch", "email": "clementine@example.com"},
]


class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(SITE_DIR), **kwargs)

    def log_message(self, format, *args):  # keep test output quiet
        pass

    # ---- helpers ----
    def _json(self, status, body, headers=None):
        data = json.dumps(body).encode()
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(data)))
        for k, v in (headers or {}).items():
            self.send_header(k, v)
        self.end_headers()
        self.wfile.write(data)

    def _body(self):
        n = int(self.headers.get("Content-Length") or 0)
        raw = self.rfile.read(n) if n else b""
        try:
            return json.loads(raw or b"{}")
        except json.JSONDecodeError:
            return {}

    def _user(self):
        for part in (self.headers.get("Cookie") or "").split(";"):
            k, _, v = part.strip().partition("=")
            if k == "session" and v.startswith(SESSION_PREFIX) and v[len(SESSION_PREFIX):] in USERS:
                return v[len(SESSION_PREFIX):]
        auth = self.headers.get("Authorization") or ""
        if auth.startswith("Bearer " + SESSION_PREFIX) and auth[len("Bearer " + SESSION_PREFIX):] in USERS:
            return auth[len("Bearer " + SESSION_PREFIX):]
        return None

    # ---- routes ----
    def do_GET(self):
        url = urlparse(self.path)
        q = parse_qs(url.query)
        if url.path == "/redirect":
            self.send_response(HTTPStatus.FOUND)
            self.send_header("Location", "/login.html")
            self.end_headers()
        elif url.path == "/api/products":
            self._json(200, PRODUCTS)
        elif url.path == "/api/users":
            self._json(200, PEOPLE)
        elif url.path.startswith("/api/users/"):
            uid = url.path.rsplit("/", 1)[-1]
            person = next((p for p in PEOPLE if str(p["id"]) == uid), None)
            self._json(200 if person else 404, person or {"error": "not found"})
        elif url.path == "/api/items":
            page = int((q.get("page") or ["1"])[0])
            items = [f"Item {i}" for i in range((page - 1) * 5 + 1, page * 5 + 1)]
            self._json(200, {"page": page, "items": items, "hasMore": page < 3})
        elif url.path == "/api/me":
            user = self._user()
            self._json(200 if user else 401, {"username": user} if user else {"error": "not signed in"})
        elif url.path == "/files/report.csv":
            data = b"name,score\ntom,90\nana,85\n"
            self.send_response(200)
            self.send_header("Content-Type", "text/csv")
            self.send_header("Content-Disposition", 'attachment; filename="report.csv"')
            self.send_header("Content-Length", str(len(data)))
            self.end_headers()
            self.wfile.write(data)
        else:
            super().do_GET()

    def do_POST(self):
        url = urlparse(self.path)
        body = self._body()
        if url.path == "/api/login":
            user, pw = body.get("username"), body.get("password")
            if USERS.get(user) == pw:
                token = SESSION_PREFIX + user
                self._json(200, {"token": token}, {"Set-Cookie": f"session={token}; Path=/; HttpOnly"})
            else:
                self._json(401, {"error": "Invalid username or password"})
        elif url.path == "/api/logout":
            self._json(200, {"ok": True}, {"Set-Cookie": "session=; Path=/; Max-Age=0"})
        elif url.path == "/api/users":
            if not body.get("name"):
                self._json(400, {"error": "name is required"})
            else:
                self._json(201, {"id": 101, **body})
        else:
            self._json(404, {"error": "not found"})

    def do_PUT(self):
        url = urlparse(self.path)
        if url.path.startswith("/api/users/"):
            self._json(200, {"id": int(url.path.rsplit("/", 1)[-1]), **self._body()})
        else:
            self._json(404, {"error": "not found"})

    def do_DELETE(self):
        url = urlparse(self.path)
        if url.path.startswith("/api/users/"):
            self.send_response(HTTPStatus.NO_CONTENT)
            self.end_headers()
        else:
            self._json(404, {"error": "not found"})


def start(port=0):
    """Start the server on a background thread. Returns (server, base_url)."""
    server = ThreadingHTTPServer(("127.0.0.1", port), Handler)
    threading.Thread(target=server.serve_forever, daemon=True).start()
    return server, f"http://127.0.0.1:{server.server_address[1]}"


if __name__ == "__main__":
    srv, base = start(8000)
    print(f"Practice site running at {base}/  (Ctrl+C to stop)")
    try:
        threading.Event().wait()
    except KeyboardInterrupt:
        srv.shutdown()

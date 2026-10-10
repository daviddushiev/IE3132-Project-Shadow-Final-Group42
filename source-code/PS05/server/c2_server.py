from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path

PORT = 8088


class Handler(BaseHTTPRequestHandler):

    def send_text(self, text):
        data = text.encode()

        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()

        self.wfile.write(data)

    def send_file(self, filename):
        path = Path(filename)

        if not path.exists():
            self.send_error(404)
            return

        data = path.read_bytes()

        self.send_response(200)
        self.send_header("Content-Type", "application/octet-stream")
        self.send_header("Content-Length", str(len(data)))
        self.send_header(
            "Content-Disposition",
            f'attachment; filename="{path.name}"'
        )
        self.end_headers()

        self.wfile.write(data)

    def do_GET(self):

        if self.path == "/beacon":
            self.send_text("OK")

        elif self.path == "/status":
            self.send_text("Solace staging service healthy")

        elif self.path == "/payload/attacker_tool":
            self.send_file("attacker_tool")

        elif self.path == "/payload/stolen_data.enc":
            self.send_file("stolen_data.enc")

        else:
            self.send_error(404)


HTTPServer(("0.0.0.0", PORT), Handler).serve_forever()

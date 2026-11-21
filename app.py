

import os
from http.server import BaseHTTPRequestHandler, HTTPServer


class WebApp(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"<h1>Welcome to my DevOps CI/CD Pipeline!</h1>")


if __name__ == "__main__":
    host = os.environ.get("HOST", "127.0.0.1")
    server = HTTPServer((host, 8000), WebApp)
    print("Web application running on port 8000")
    server.serve_forever()


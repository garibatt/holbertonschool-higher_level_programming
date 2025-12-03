#!/usr/bin/python3
"""
commit for task
"""

from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class SimpleAPIHandler(BaseHTTPRequestHandler):

    def _set_headers(self, status=200, content_type="text/plain"):
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.end_headers()

    def do_GET(self):
        if self.path == "/":
            self._set_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        elif self.path == "/data":
            data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }
            self._set_headers(content_type="application/json")
            self.wfile.write(json.dumps(data).encode("utf-8"))

        elif self.path == "/status":
            self._set_headers(content_type="application/json")
            self.wfile.write(b"OK")

        elif self.path == "/info":
            info = {
                "version": "1.0",
                "description": "A simple API built with http.server"
            }
            self._set_headers(content_type="application/json")
            self.wfile.write(json.dumps(info).encode("utf-8"))

        else:
            # Unknown endpoint → 404
            self._set_headers(status=404)
            self.wfile.write(b"Endpoint not found")


def run(server_class=HTTPServer, handler_class=SimpleAPIHandler):
    port = 8000
    server_address = ("", port)
    httpd = server_class(server_address, handler_class)
    print(f"Serving on port {port}...")
    httpd.serve_forever()


if __name__ == "__main__":
    run()


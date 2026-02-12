#!/usr/bin/python3
import http.server
import socketserver
import json


class SimpleAPIHandler(http.server.BaseHTTPRequestHandler):
    """
    A custom request handler to manage specific API endpoints.
    """

    def do_GET(self):
        """Handles GET requests based on the URL path."""

        if self.path == '/':
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        elif self.path == '/data':
            data = {"name": "John", "age": 30, "city": "New York"}
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(data).encode('utf-8'))

        elif self.path == '/status':
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")

        else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Endpoint not found")


def run_server():
    """Starts the HTTP server on port 8000."""
    PORT = 8000
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("", PORT), SimpleAPIHandler) as httpd:
        print(f"Serving at port {PORT}")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            httpd.server_close()


if __name__ == "__main__":
    run_server()

#!/usr/bin/python3
"""
Task 3: Develop a simple API using Python with the `http.server` module
"""

from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class SimpleAPIHandler(BaseHTTPRequestHandler):
    """Request Handler for a simple API"""

    def _send_text(self, status_code, message):
        """Sends a plain text response"""
        self.send_response(status_code)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.end_headers()
        self.wfile.write(message.encode("utf-8"))
        
    def _send_json(self, status_code, payload):
        """Send a JSON response."""
        self.send_response(status_code)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(payload).encode("utf-8"))

    def do_GET(self):
        """Handle GET requests"""
        if self.path == "/":
            self._send_text(200, "Hello, this is a simple API!")
        elif self.path == "/status":
            self._send_text(200, "OK")
        elif self.path == "/data":
            self._send_json(200, {"name": "John", "age": 30, "city": "New York"})
        elif self.path == "/info":
            self._send_json(
                200,
                {"version": "1.0", "description": "A simple API built with http.server"}
            )
        else:
            self._send_text(404, "Endpoint not found")

    def log_message(self, format, *args):
        """Optional: keep default logging style but you can silence logs here."""
        super().log_message(format, *args)

def run(server_class=HTTPServer, handler_class=SimpleAPIHandler, port=8000):
    """Start the HTTP server."""
    server_address = ("", port)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()

if __name__ == "__main__":
    run()

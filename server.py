#!/usr/bin/env python3
import http.server
import socketserver
import os
from http.server import SimpleHTTPRequestHandler

class NoCacheHTTPRequestHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()

class ReusableTCPServer(socketserver.TCPServer):
    allow_reuse_address = True

if __name__ == "__main__":
    PORT = int(os.environ.get("PORT", 5000))
    Handler = NoCacheHTTPRequestHandler
    
    print(f"Starting server on port {PORT}")
    with ReusableTCPServer(("0.0.0.0", PORT), Handler) as httpd:
        print(f"Server successfully started at http://0.0.0.0:{PORT}")
        httpd.serve_forever()
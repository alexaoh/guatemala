#!/usr/bin/env python3
"""Simple CLI to serve the Guatemala travel website."""

import http.server
import socketserver
import os

def main():
    """Start the HTTP server on port 8000."""
    port = 8000
    handler = http.server.SimpleHTTPRequestHandler

    with socketserver.TCPServer(("", port), handler) as httpd:
        print(f"Serving at http://localhost:{port}")
        print("Press Ctrl+C to stop the server.")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServer stopped.")

if __name__ == "__main__":
    main()
from http.server import BaseHTTPRequestHandler, HTTPServer
import sys

class HelloHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain; charset=utf-8")
        self.end_headers()
        self.wfile.write(b"Hello World from AWS EC2 via Jenkins Pipeline!")

if __name__ == "__main__":
    print("Starting server on 0.0.0.0:8000...", flush=True)
    server = HTTPServer(("0.0.0.0", 8000), HelloHandler)
    server.serve_forever()
from http.server import SimpleHTTPRequestHandler, HTTPServer

class HelloHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b"Hello World from AWS EC2 via Jenkins!")

server = HTTPServer(("0.0.0.0", 8000), HelloHandler)
print("Serving on port 8000...")
server.serve_forever()
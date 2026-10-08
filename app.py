from http.server import SimpleHTTPRequestHandler, HTTPServer

class HelloHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        # Updated message to verify new deployment
        self.wfile.write(b"Hello World v2: Successfully deployed via Jenkins Pipeline!")

server = HTTPServer(("0.0.0.0", 8000), HelloHandler)
print("Serving on port 8000...")
server.serve_forever()
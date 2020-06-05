from http.server import BaseHTTPRequestHandler, HTTPServer


class testHTTPServer_RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write((bytes("This is as alternate file", "utf8")))
        return


def run():
    httpd = HTTPServer(('0.0.0.0', 8080), testHTTPServer_RequestHandler)
    httpd.serve_forever()


run()

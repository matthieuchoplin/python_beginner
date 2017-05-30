import http.server
import socketserver


class WebserverHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        try:
            self.send_response(200)
            self.send_header('Content-Type', 'text/html')
            self.end_headers()

            output = ""
            output += "<html><body>Hello</body></html>"
            self.wfile.write(output)
            print(output)
            return
        except IOError:
            self.send_error(404, "File not Found %s" % self.path)


def main():
    httpd = socketserver.TCPServer(('', 8000), WebserverHandler)
    httpd.serve_forever()

main()
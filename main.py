from http.server import HTTPServer, BaseHTTPRequestHandler

from config import CONFIG
import kmlgenerator


class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/data.kml":
            try:
                contents = kmlgenerator.generate()
                self.send_response(200)
                self.send_header("Content-type", "Content-Type: application/vnd.google-earth.kml+xml")
                self.end_headers()
                print(contents)
                self.wfile.write(bytes(contents, "utf-8"))
            except Exception as e:
                self.send_response(500)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write(bytes("Internal server error: " + str(e), "utf-8"))
        else:
            self.send_response(404)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(bytes("<html><head><title>UISP to KML</title></head>", "utf-8"))
            self.wfile.write(bytes("<body>", "utf-8"))
            self.wfile.write(bytes("<p>%s: not found</p>" % self.path, "utf-8"))
            self.wfile.write(bytes("</body></html>", "utf-8"))


# When `python main.py` is run, this code is executed
if __name__ == "__main__":
    webServer = HTTPServer((CONFIG.HOSTNAME, CONFIG.PORT), MyServer)
    print("Server started http://%s:%s" % (CONFIG.HOSTNAME, CONFIG.PORT))

    try:
        webServer.serve_forever()
    # Ctrl + C
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")

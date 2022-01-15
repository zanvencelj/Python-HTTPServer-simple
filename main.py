from http.server import BaseHTTPRequestHandler, HTTPServer

hostName = "192.168.0.104"
serverPort = 8080

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/on":
            print("LED on")
        elif self.path == "/off":
            print("LED off")
        else:
            print("neki je")

if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), MyServer)

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")

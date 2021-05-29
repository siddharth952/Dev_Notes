from http.server import BaseHTTPRequestHandler, HTTPServer #!Basic Securtiy do not use in production
import cgi

# handler - What code to execute based on HttpCode
class WebServerHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            if self.path.endswith("/hello"):
                self.send_response(200)
                #web server is already sending the text encoded to UTF-8 but you need to tell your browser the encoding of the bytes it receives. The HTTP spec. declares ISO-8995-1 as the default.
                self.send_header('Content-type', 'text/html; charset=utf-8')
                self.end_headers()
                message = ''
                message += "<html><body>Hello!</body></html>"
                self.wfile.write(bytes(message,'UTF-8'))
                print( message)
                return
        
            if self.path.endswith("/hola"):
                self.send_response(200)
                #web server is already sending the text encoded to UTF-8 but you need to tell your browser the encoding of the bytes it receives. The HTTP spec. declares ISO-8995-1 as the default.
                self.send_header('Content-type', 'text/html; charset=utf-8')
                self.end_headers()
                message = ''
                message += "<html><body>&#161Hola <a href = '/hello'> Back to Home</a> </body></html>"
                self.wfile.write(bytes(message,'UTF-8'))
                print( message)
                return
        except:
            self.send_error(404,"File not Found",self.path)
    
    def do_POST(self):
        try:
            self.send_response(301)
            self.end_headers()
        except:

def main():
    try:
        port = 8080
        server = HTTPServer(('',port), WebServerHandler )
        print("Web server is running on port:",port)
        server.serve_forever()
    
    except KeyboardInterrupt:
        print("^C entered. Stopping the server....")
        server.socket.close()


if __name__ == '__main__':
    main()

from http.server import HTTPServer, CGIHTTPRequestHandler
server_address = ("", 9090)
httpd = HTTPServer(server_address, CGIHTTPRequestHandler)
httpd.serve_forever()
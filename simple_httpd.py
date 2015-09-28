#!/usr/bin/env python

#from http.server import HTTPServer, CGIHTTPRequestHandler
#from BaseHTTPServer import CGIHTTPServer, CGIHTTPRequestHandler
import cgitb
cgitb.enable()
import BaseHTTPServer
import CGIHTTPServer
 ## This line enables CGI error report
port = 8001
server = BaseHTTPServer.HTTPServer
handler = CGIHTTPServer.CGIHTTPRequestHandler
server_address = ("", port)
handler.cgi_directories = ['/cgi-bin']
 
httpd = server(server_address, handler)
print("Starting simple_httpd on port: " + str(httpd.server_port))
httpd.serve_forever()

#httpd = HTTPServer(('', port), CGIHTTPRequestHandler)
#print("Starting simple_httpd on port: " + str(httpd.server_port))
#httpd.serve_forever()


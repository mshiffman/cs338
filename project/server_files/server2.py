# Created by Osareme Davis
# based heavily on example from https://gist.github.com/scimad/ae0196afc0bade2ae39d604225084507
import http.server
import socketserver
import urllib.parse

class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        http.server.SimpleHTTPRequestHandler.end_headers(self)

    def do_GET(self):
        if self.path == '/':
            self.path = 'index.html'
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

    def do_POST(self):
        self.path = 'index.html'
        # need to do something else here to get formatting right
        content_length = int(self.headers['Content-Length'])
        post_data_bytes = self.rfile.read(content_length)
        post_data_str = post_data_bytes.decode("UTF-8")  
        post_data_str = urllib.parse.unquote_plus(post_data_str[5:])
        post_file = open('post.html', 'w')
        post_file.write(post_data_str)
        post_file.close()          
        return http.server.SimpleHTTPRequestHandler.do_GET(self)
 

# Create an object of the above class
handler_object = MyHttpRequestHandler

PORT = 8000
my_server = socketserver.TCPServer(("", PORT), handler_object)

# Start the server
my_server.serve_forever()
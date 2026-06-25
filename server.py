from http.server import HTTPServer, SimpleHTTPRequestHandler
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

class Handler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        super().end_headers()

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    server = HTTPServer(('0.0.0.0', port), Handler)
    print(f'Serving artifacts on :{port}')
    server.serve_forever()

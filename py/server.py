from http.server import BaseHTTPRequestHandler, HTTPServer
import time

from py.processors import Browser
from py.stripper import Medium, Others
import py.utils as ut


br = Browser()

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        url = self.path.lstrip('/')
        print("accessing url", url)

        if not ut.is_valid_url(url):
            self.send_response(400)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(bytes("invalid url",'utf-8'))
            return

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        fname = f'/tmp/{ut.hashit(url)}.html'

        if ut.is_file_present(fname):
            self.wfile.write(ut.read(fname).encode('utf-8'))
            return

        data = br.dump(url)
        # ut.write('/tmp/test.html', data)

        m = Medium()
        if "medium" not in url:
            print("using non medium, stripping all script tags")
            m = Others()
        v =  m.strip_scripts_with_src(data)
        ut.write(fname, v)

        # print(v, "v")

        self.wfile.write(ut.read(fname).encode('utf-8'))



import sys
from http.server import  HTTPServer

from py.processors import Browser
from py.stripper import Medium
from py.server import MyServer
import py.utils as ut


def render_page(url: str):
    br = Browser()
    fname = f'/tmp/{ut.hashit(url)}.html'

    if ut.is_file_present(fname):
        br.open(fname) 
        return

    data = br.dump(url)
    # ut.write('/tmp/test.html', data)

    m = Medium()
    v =  m.strip_scripts_with_src(data)
    ut.write(fname, v)
    br.open(fname) 


def start_server():
    hostName = "0.0.0.0"
    serverPort = 8741 

    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")

if __name__ == "__main__":
    command = sys.argv[1]
    
    if not command:
        print("invalid command, either url or command not provided")
        sys.exit(1)

    if ut.is_valid_url(command):
        render_page(command)
        sys.exit(0)

    if command == "server":
        start_server()
        sys.exit(0)
    
    print("invalid command, either url or command not provided")
    sys.exit(2)



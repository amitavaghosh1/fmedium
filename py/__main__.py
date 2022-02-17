import sys

import py.fetch as fetch
from py.processors import Browser
from py.stripper import Medium
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



if __name__ == "__main__":
    url = sys.argv[1]
    if not url:
        print("url not provided")
        sys.exit(1)
    if not ut.is_valid_url(url):
        print("invalid url")
        sys.exit(2)

    render_page(url)

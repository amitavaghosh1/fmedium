import subprocess
# import signal
import os

from py.cmd import chrome

def page_with_chrome(url: str):
    command = [
            chrome(),
            '--headless',
            '--disable-gpu',
            '--crash-dumps-dir=/tmp',
            '--dump-dom'
    ]
    command = ' '.join(command)
    p = subprocess.Popen(
            f'{command} "{url}"',
            shell=True,
            stdout=subprocess.PIPE,
            executable=os.environ['SHELL'])

    contentb = p.communicate()[0]
    return contentb.decode('utf-8')



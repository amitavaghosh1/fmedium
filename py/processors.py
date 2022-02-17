import subprocess
import os

from py.cmd import chrome

class Browser:
    def __init__(self):
        self.executable = chrome()

    def dump(self, url: str):
        command = [
                self.executable,
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
 
    def open(self, url: str):
        command = self.executable
        try:
            p = subprocess.Popen(
                    f'{command} "{url}"',
                    close_fds = True,
                    shell=True,
                    stdout=subprocess.PIPE,
                    executable=os.environ['SHELL']
                )
        except Exception as e:
            print(e)


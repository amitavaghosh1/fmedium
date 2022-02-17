from html.parser import HTMLParser

class GenHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.reset()
        self.strict = False
        self.convert_charrefs = True
        self.skip = False
        self.data = []

    def handle_startendtag(self, tag, attrs):
        pass
    
    def handle_endtag(self, tag):
        pass

    def handle_data(self, data):
        self.data.append(str(data))

    def get_data(self):
        return ' '.join(self.data)

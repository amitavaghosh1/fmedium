# import xml.dom.minidom
# from lxml import etree, html

# def format_html(s: str) -> str:
    # return xml.dom.minidom.parseString(s).toprettyxml()


# def format_html(s: str) -> str:
    # document_root = html.fromstring(s)
    # return etree.tostring(document_root, encoding='unicode', pretty_print=True)

from py.parser import GenHTMLParser

def format_html(s: str) -> str:
    g = GenHTMLParser
    g.feed(s)
    return g.get_data()

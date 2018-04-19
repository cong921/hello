# -*- coding: utf-8 -*-
'''
Created on 2018��4��15��

@author: Bob
'''

from html.parser import HTMLParser
from html.entities import name2codepoint
from urllib import request

class MyHTMLParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        if tag=='h3' :
            for key in attrs:
#                 print(key)
                if key==('class', 'event-title'):
#                     print(self.handle_data())
                    print('<%s>' % "abc")
        return
#     def handle_endtag(self, tag):
#         print('</%s>' % tag)
# 
#     def handle_startendtag(self, tag, attrs):
#         print('<%s/>' % tag)
# 
#     def handle_data(self, data):
#         print(data)
# 
#     def handle_comment(self, data):
#         print('<!--', data, '-->')
# 
    def handle_entityref(self, name):
        print('&%s;' % name)
# 
#     def handle_charref(self, name):
#         print('&#%s;' % name)

parser = MyHTMLParser()
with request.urlopen("https://www.python.org/events/python-events/", timeout=5) as f:
    data = f.read()
parser.feed(data.decode('utf-8'))

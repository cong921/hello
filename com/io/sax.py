# -*- coding: utf-8 -*-
'''
Created on 2018��4��15��

@author: Bob
'''

from xml.parsers.expat import ParserCreate
from xml.sax.saxutils import handler
from urllib import request

def parseXml(xml_str):
    
#     print(xml_str)
    dict={}
    everyday={}
    class DefaultSaxHandler(object):
        def start_element(self, name, attrs):
            for i in attrs:
                print(i)
                if i=='city':
                    dict[i]=attrs[i]
    #         if('city'.index(attrs)!=-1):
    #             print('sax:start_element: %s, attrs: %s' % (name, str('city')))
    
        def end_element(self, name):
            pass
    #         print('sax:end_element: %s' % name)
    
        def char_data(self, text):
            pass
#         print('sax:char_data: %s' % text)
    handler = DefaultSaxHandler()   
    parser = ParserCreate()
    parser.StartElementHandler = handler.start_element
    parser.EndElementHandler = handler.end_element
    parser.CharacterDataHandler = handler.char_data
    parser.Parse(xml_str)
    print(dict['city'])
    return {
        'city': dict['city'],
        'forecast': [
            {
                'date': '2017-11-17',
                'high': 43,
                'low' : 26
            },
            {
                'date': '2017-11-18',
                'high': 41,
                'low' : 20
            },
            {
                'date': '2017-11-19',
                'high': 43,
                'low' : 19
            }
        ]
    }
    
# 测试:
URL = 'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=xml'

with request.urlopen(URL, timeout=4) as f:
    data = f.read()

result = parseXml(data.decode('utf-8'))
assert result['city'] == 'Beijing'

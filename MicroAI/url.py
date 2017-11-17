#coding=utf-8
'''
the url structure of website
'''

from handlers.index import IndexHandler
from handlers.result import ResultHandler

url = [
    (r'/', IndexHandler),
    (r'/res', ResultHandler)
] 
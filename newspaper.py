#coding=utf-8
import urllib

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

html = getHtml("http://news01.hit.edu.cn/class/92_5_0.htm")

print html
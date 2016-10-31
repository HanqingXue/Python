#coding=utf-8
import urllib
import HTMLParser

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

def getTitle(html):
    print type(html)

html = getHtml("http://news01.hit.edu.cn/class/92_5_0.htm")

values = []
class MyParser(HTMLParser.HTMLParser):
    def __init__(self):
        HTMLParser.HTMLParser.__init__(self)

    def handle_starttag(self, tag, attrs):
        # 这里重新定义了处理开始标签的函数
        if tag == 'a':
            # 判断标签<a>的属性
            for name, value in attrs:
                if name == 'href':
                    if 'class' in value:
                        continue
                    print value
                    values.append(value)

if __name__ == '__main__':
    a = getHtml("http://news01.hit.edu.cn/class/92_5_0.htm")

    my = MyParser()
    # 传入要分析的数据，是html的。
    my.feed(a)
    for item in values:
        url = "http://news01.hit.edu.cn/" + item
        print url
        content = getHtml(url)
        out = open('./html/'+item[-12:-4]+'.html', 'w')
        out.write(content)

    f = open('./html/01083921.html')
    for item in f:
        if '<title>' in item:
            print item



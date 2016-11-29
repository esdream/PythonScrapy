# coding:utf-8
import urllib
import urllib2

# 由于糗事百科网站爬取时会返回奇怪的东西。。。此程序暂时作废
page = 1
url = 'http://www.qiushibaike.com/hot/'
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36'
header = {'User_Agent': user_agent}
try:
    request = urllib2.Request(url, headers = header)
    response = urllib2.urlopen('request')
    print(response.read())
except urllib2.URLError, e:
    if hasattr(e, 'code'):
        print e.code
    if hasattr(e, 'reason'):
        print e.reason

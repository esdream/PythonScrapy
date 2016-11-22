import urllib2

res = urllib2.urlopen('http://www.baidu.com')
print(res.read())

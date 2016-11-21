import urllib
import urllib2

# 该网址只是一个案例，并不能真正运行
url = 'http://www.someserver.com/register.cgi'
values = {
    'name': 'WHY',
    'location': 'SDU',
    'language': 'python'
}

data = urllib.urlencode(values)
req = urllib2.Request(url, data)
response = urllib2.urlopen(req)
the_page = response.read()

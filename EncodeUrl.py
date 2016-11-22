# coding: utf-8
import urllib
import urllib2

# POST方式
url = 'http://www.someserver.com/register.cgi'
values1 = {
    'name': 'WHY',
    'location': 'SDU',
    'language': 'python',
    'password': 'faizalfu'
}

data = urllib.urlencode(values1)
print(data)
req = urllib2.Request(url, data)
response = urllib2.urlopen(req)
the_page = response.read()

# GET方式
values2 = {}
values2['username'] = 'esdream'
values2['password'] = 'like'
data2 = urllib.urlencode(values2)
url = 'http://passport.csdn.net/account/login'
geturl = url + '?' + data2
request = urllib2.Request(geturl)
print(request)
response2 = urllib2.urlopen(request)
print(response2.read())

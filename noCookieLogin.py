import urllib2

f1 = open('./test.html', 'w')
req = urllib2.Request('http://www.acfun.tv/member/#area=profile')
res = urllib2.urlopen(req)
f1.write(res.read())
f1.close()

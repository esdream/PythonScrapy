from urllib2 import Request, urlopen, URLError, HTTPError
req = Request('http://bbs.csdn.net/callmewhy')
try:
    response = urlopen(req)
except URLError, e:
    if hasattr(e, 'code'):
        print('Error code: ', e.code)
    elif hasattr(e, 'reason'):
        print('Reson:', e.reason)
else:
    print 'No exception was raised.'

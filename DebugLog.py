import urllib2
httpHandler = urllib2.HTTPHandler(debuglevel=1)
# httpsHandler = urllib2.HTTPShandler(debuglevel=1)
opener = urllib2.build_opener(httpHandler)
urllib2.install_opener(opener)
response = urllib2.urlopen('http://www.baidu.com')

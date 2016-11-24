import urllib2
import cookielib

filename = 'acfunCookie.txt'
writeCookie = cookielib.MozillaCookieJar(filename)
handler = urllib2.HTTPCookieProcessor(writeCookie)

opener = urllib2.build_opener(handler)
res = opener.open('http://www.acfun.tv')
writeCookie.save(ignore_discard = True, ignore_expires = True)

# coding:utf-8
import urllib2
import cookielib

filename = 'cookie.txt'
# 声明一个CookieJar对象实例来保存cookie
writeCookie = cookielib.MozillaCookieJar(filename)
# 利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
handler = urllib2.HTTPCookieProcessor(writeCookie)
# 通过handler来创建opener
opener = urllib2.build_opener(handler)
res = opener.open('https://www.baidu.com')
for item in writeCookie:
    print('Name = ' + item.name)
    print('Value = ' + item.value)
writeCookie.save(ignore_discard = True, ignore_expires = True)

readCookie = cookielib.MozillaCookieJar()
# 从文件中读取cookie内容到变量
readCookie.load('cookie.txt', ignore_discard=True, ignore_expires=True)
# 利用urllib2的build_opener方法创建一个opener
readOpener = urllib2.build_opener(urllib2.HTTPCookieProcessor(readCookie))
res = readOpener.open('https://www.baidu.com')
print(res.read())

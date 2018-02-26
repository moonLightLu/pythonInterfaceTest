# -*- coding:utf-8 -*-
#发送cookie到服务器

import requests
import json

url = "http://httpbin.org/get"

#方法1：简单发送
#cookies = {"aaa":"bbb"}
#r = requests.get(url,cookies = cookies)
#print r.text

#方法2：复杂发送
s = requests.session()
c = requests.cookies.RequestsCookieJar()
c.set('c-name', 'c-value',path = '/xxx/uuu',domain = '.test.com')
s.cookies.update(c)
r = requests.get(url,cookies = c)
print r.text
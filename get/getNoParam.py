#-*- coding:utf-8 -*-
#不带参数的get请求

import requests
import json

host = "http://httpbin.org/"
endpoint = "get"

url = ''.join ([host,endpoint])
r = requests.get(url)

print type(r.text)
print (eval(r.text))
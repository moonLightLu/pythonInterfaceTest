# -*- coding:utf-8 -*-
#带参数的get请求

import requests
import json

host = "http://httpbin.org/"
endpoint = "get"

url = ''.join([host,endpoint])
headers = {"User-Agent":"test request header"}

r = requests.get(url)
r = requests.get(url,headers = headers)

print (eval(r.text))['headers']['User-Agent']
print (eval(r.text))

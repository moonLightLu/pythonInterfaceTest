# -*- coding:utf-8 -*-
#带header的post请求

import requests
import json

host = "http://httpbin.org/"
endpoint = "post"

url = ''.join([host,endpoint])
headers = {'User-Agent':'test request header'}

r = requests.post(url,headers = headers)

response = r.json()
print r.text
print response
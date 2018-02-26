# -*- coding:utf-8 -*-
#流式上传

import requests
import json

host = "http://httpbin.org/"
endpoint = "post"

url = ''.join([host,endpoint])

with open('text.txt') as f:
	r = requests.post(url,data = f)

print r.text
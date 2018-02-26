# -*- coding:utf-8 -*-
#带json的post请求

import requests
import json

host = "http://httpbin.org/"
endpoint = "post"

url = ''.join([host,endpoint])
data = {
	"site":[
			{"name":"test","url":"www.test.com"},
			{"name":"google","url":"www.google.com"},
			{"name":"weibo","url":"www.weibo.com"}
	]
}

r = requests.post(url,json=data)

print r.text
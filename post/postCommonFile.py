# -*- coding:utf-8 -*-
#普通文件上传

import requests
import json

host = "http://httpbin.org/"
endpoint = "post"

url = ''.join([host,endpoint])

files = {
			'file':open('E:/pythonHttp/text.txt','rb')
}

r = requests.post(url,files = files)

print (r.text)
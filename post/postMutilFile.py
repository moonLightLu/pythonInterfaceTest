# -*- coding:utf-8 -*-
#多文件上传

import requests
import json

host = "http://httpbin.org/"
endpoint = "post"

url = ''.join([host,endpoint])

files = [
			('file1',('text.txt',open('text.txt','rb'))),
			('file2',('1.jpg',open('1.jpg','rb'),'image/jpg'))
]

r = requests.post(url,files = files)

print r.text
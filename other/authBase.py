# -*- coding:utf-8 -*-
#基本认证

import requests

url = "http://httpbin.org/basic-auth/user/passwd"

r1 = requests.get(url)
print "未提供用户名密码：" + str(r1.status_code)

#Basic Authentication
r2 = requests.get(url,auth = ('user','passwd'))
print "已提供用户名密码：" + str(r2.status_code)
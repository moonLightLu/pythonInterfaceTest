# -*- coding:utf-8 -*-
#proxy参数

import requests

proxies = {
  "https": "http://41.118.132.69:4433"
}
r = requests.post("http://httpbin.org/post", proxies=proxies,timeout = 5)  #利用timeout参数来配置最大请求时间
#r = requests.get('https://github.com', timeout=None)   #设置timeout=None，告诉请求永远等待响应，而不将请求作为超时值传递
print r.text


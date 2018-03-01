# -*- coding:utf-8 -*-
#提供默认数据

import requests
import json

s = requests.session()
s.auth = ('user','pass')
s.headers.update({"x-test":"true"})

# both 'x-test' and 'x-test2' are sent
r = s.get("http://httpbin.org/headers",headers = {"x-test2":"true"})

print r.text
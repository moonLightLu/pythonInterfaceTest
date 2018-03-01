# -*- coding:utf-8 -*-
#O认证

import requests
from requests.auth import HTTPDigestAuth

url = "http://httpbin.org/digest-auth/auth/user/passwd"
r = requests.get(url, auth=HTTPDigestAuth('user', 'passwd'))

print str(r.status_code)
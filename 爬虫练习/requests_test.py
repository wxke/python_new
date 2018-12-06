#!/usr/bin/env python
# -*- coding:UTF-8 -*-
import requests
request = requests.get("http://www.baidu.com")
print(type(request))
print(request)
print(request.text)
print(request.history)
print(1) if 1==1 else print(2)


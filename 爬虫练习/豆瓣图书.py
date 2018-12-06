#!/usr/bin/env python
# -*- coding:UTF-8 -*-
import re
import requests

request = requests.get("https://book.douban.com").text
request = re.sub("&nbsp;",'',request)
com = re.compile('<li.*?class="cover".*?<a\shref="(.*?)"\stitle="(.*?)".*?<div class="author">(.*?)</div>.*?</li>',re.S)
req = re.findall(com,request)
for i in req:
    print(i[0].strip(),i[1].strip(),i[2].strip())

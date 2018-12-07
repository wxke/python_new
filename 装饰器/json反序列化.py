#!/usr/bin/env python
# -*- coding:UTF-8 -*-

import json

f = open('test.txt','r')

data = json.loads(f.read())
print(data)

f.close()
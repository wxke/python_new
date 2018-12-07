#!/usr/bin/env python
# -*- coding:UTF-8 -*-
import json
info = {
    'name':'wxk',
    'age' : '21'
}

f = open('test.txt','w')

f.write(json.dumps(info))

f.close()
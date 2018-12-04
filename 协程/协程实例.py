#!/usr/bin/env python
# -*- coding:UTF-8 -*-
import gevent,time
from urllib import request
from gevent import monkey


monkey.patch_all()
def f(url):
    print("down ..... %s" %url)
    res = request.urlopen(url)


    #data = res.read()
    #print("%s bytes received from %s " %(len(data),url))

'''
url = ["https://www.python.org","https://www.douban.com/","https://www.zhihu.com"]
b = time.time()
for i in url:
    f(i)

print("串行时间 ",time.time()-b)
'''


#a = time.time()
gevent.joinall(
    [gevent.spawn(f,'http://10.90.16.90/') for i in range(1,1000000)]




)
#print("并行 ",time.time()-a)
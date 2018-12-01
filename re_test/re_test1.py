#!/usr/bin/env python
# -*- coding:UTF-8 -*-
import re

# res = re.match("^w.",'wx k123wxk')
# print(res)
# print(res.group())
'''
. 匹配除/n 的第一个字符
^ 匹配字符开头
+ 匹配一次或多次
? 匹配前一个字符一次或零次 re.search('aa  a?','aa1231aaa') 就是问号前面字符
'''
res = re.search('#.+#','123#holle#123')
print(res)
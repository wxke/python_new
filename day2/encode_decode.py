#!/usr/bin/env python
# -*- coding:UTF-8 -*-
msg = "某某"

print(msg.encode("utf-8"))#其中utf-8是默认，若msg是什么其中就是什么
msg1 = b'\xe7\x8e\x8b\xe6\x99\x93\xe7\xa7\x91'
print(msg1.decode("utf-8"))#同上

#encode 是将把字符转化为二进制
#decode 是将把二进制转化为字符

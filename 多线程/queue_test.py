#!/usr/bin/env python
# -*- coding:UTF-8 -*-
import queue

# q = queue.Queue()  #在括号中可以设置队列长度
# q.put("1")
# print(q.full())  #是否为满
# print(q.qsize())
# print(q.get())

#print(q.get_nowait())


q = queue.LifoQueue()  #堆
q.put(1)
q.put(2)
q.put(3)
print(q.get())
print(q.get())
print(q.get())

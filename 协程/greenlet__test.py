#!/usr/bin/env python
# -*- coding:UTF-8 -*-
import greenlet


def run():
    print(12)                                #2
    g2.switch()                              #3
    print(56)                                #6
    g2.switch()                              #7


def run2():
    print(34)                                #4
    g1.switch()                              #5
    print(78)                                #8


g1 = greenlet.greenlet(run)
g2 = greenlet.greenlet(run2)

g1.switch()  #遇到一个switch 就跳转到相应的地方   #1
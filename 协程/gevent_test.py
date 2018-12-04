#!/usr/bin/env python
# -*- coding:UTF-8 -*-

import gevent


def run1():
    print("running >>>>>>>>:1  0")
    gevent.sleep(2)
    print("running >>>>>>>>:1  1")

def run2():
    print("running >>>>>>>>:2  0")
    gevent.sleep(1)
    print("running >>>>>>>>:2  1")

def run3():
    print("running >>>>>>>>:3  0")
    gevent.sleep(0)
    print("running >>>>>>>>:3  1")


gevent.joinall(
    [
        gevent.spawn(run1),
        gevent.spawn(run2),
        gevent.spawn(run3)
    ]
)
#!/usr/bin/env python
# -*- coding:UTF-8 -*-
import time

def timer(func):
    def jishi(*args,**kwargs):
        star_time = time.time()
        func(*args,**kwargs)
        stop_time = time.time()
        print("this func run time ",stop_time-star_time)
    return jishi

@timer  #func() = test1() test1 = timer(func)  test1() = jishi()
def test1():
    time.sleep(1)
    print("in the text1")
@timer
def test2(name):
    time.sleep(1)
    print("in the text2",name)

test1()
test2('wxk')

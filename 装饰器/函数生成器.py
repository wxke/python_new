#!/usr/bin/env python
# -*- coding:UTF-8 -*-
def fib(max):
    n,a,b=0,0,1
    while n <max:
        yield b  #重点
        a,b = b,a+b
        n = n+1


f = fib(5)
print(f.__next__())
print(f.__next__())
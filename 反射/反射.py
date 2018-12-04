#!/usr/bin/env python
# -*- coding:UTF-8 -*-
def talk(self):
    print("%s talking!!!!!!!!!" %self.name)
class dog(object):
    def __init__(self,name):
        self.name = name

    def walk(self):
        print('%s walking!!!!!!!!'%self.name)


d = dog("啦啦啦")
d.walk()
chioce = input(">>>>:")

if hasattr(d,chioce):
    func = getattr(d,chioce)
    func()
else:
    setattr(d,chioce,talk)
    func = getattr(d,chioce)
    func(d)


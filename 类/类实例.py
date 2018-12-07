#!/usr/bin/env python
# -*- coding:UTF-8 -*-
class Foo():
    def __init__(self,name):
        self.name = name
    def showname(self):
        print(self.name)




obj = Foo("wxk")
obj.showname()
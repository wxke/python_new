#!/usr/bin/env python
# -*- coding:UTF-8 -*-

import threading
import time

class Mythread(threading.Thread):
    def __init__(self,name):
        super(Mythread, self).__init__()
        self.name = name


    def run(self):
        print(self.name)
        time.sleep(2)





t1 = Mythread("t1")

t2 = Mythread("t2")

t1.start()
t2.start()



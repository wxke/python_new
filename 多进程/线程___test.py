#!/usr/bin/env python
# -*- coding:UTF-8 -*-
import multiprocessing
import time

def run():
    time.sleep(1)
    print("run >>>>>>>>>>")


if __name__ =='__main__':
    t = multiprocessing.Process(target=run,)
    t.start()

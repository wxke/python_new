#!/usr/bin/env python
# -*- coding:UTF-8 -*-
import multiprocessing
import time , os

def run(args):
    time.sleep(2)
    print("\033[41;1m%s=======进程中\033[0m"%os.getpid())
    return args+100


def Buuf(args):
    print("%s======进程回调"%os.getpid())



if __name__ == '__main__':
    pool = multiprocessing.Pool(processes=5)

    for i in range(10):
        #pool.apply_async(func=run,args=(i,), callback=Buuf)  #并行
        pool.apply(func=run,args=(i,))  #串行

    print("end")


    pool.close()
    pool.join()



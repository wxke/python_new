#!/usr/bin/env python
# -*- coding:UTF-8 -*-

import threading
import time

def run():
    lock.acquire()  #线程锁 关闭
    global n
    n += 1
    print(n)
    lock.release()  #线程锁  释放

n = 0

lock = threading.Lock()  #线程锁
                         #threading.RLock() 递归锁
                         #semaphore = threading.BoundedSemaphore(5) 信号量 最多允许多少个线程一起运行
for i in range(50):
    t = threading.Thread(target=run)
    #t.setDaemon(True)   #设置守护线程  就不会理会守护线程是不是运行完  而在乎其他子线程  主程序运行完会直接关闭
    t.start()

print("doing----done")

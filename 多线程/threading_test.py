#!/usr/bin/env python
# -*- coding:UTF-8 -*-


import threading
import time
#主线程是程序本身  一下都是在本线程的“子线程”

def run(n):
    print("start:---",n)
    time.sleep(2)
    print("end:-----",n)

list = []
start_time = time.time()
for i in range(50):
    t = threading.Thread(target=run,args=("----%s" %i ,))
    t.start()
    list.append(t)

print(list)
for t in list:
    t.join()    #等待所有进程结束



print("总时间",time.time()  - start_time )



# t1 = threading.Thread(target=run,args=("t1",))
# t2 = threading.Thread(target=run,args=("t2",))
# t1.start()
# t2.start()

# run("t1")
# run("t2")
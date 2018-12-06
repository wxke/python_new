#!/usr/bin/env python
# -*- coding:UTF-8 -*-
import threading
import time

event = threading.Event()

count = 0

while True:
    if count >5 and count <10:
        event.clear()
        print("\033[41;1mred\033[0m")
        time.sleep(1)
    elif count >10:
        event.set()
        time.sleep(1)
        count = 0
    else:
        print("\033[42;1mgreen\033[0m")
        time.sleep(1)
    count  = count + 1





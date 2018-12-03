#!/usr/bin/env python
# -*- coding:UTF-8 -*-
import socket

clien = socket.socket()

clien.connect(("localhost",8000))
while True:
    a = input(">>>:").strip()
    if len(a) == 0:
        continue
    clien.send(a.encode("utf-8"))
    data = clien.recv(10240000)
    print("clien recv:",data.decode())

clien.close()

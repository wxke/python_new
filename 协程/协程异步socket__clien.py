#!/usr/bin/env python
# -*- coding:UTF-8 -*-
import socket


c =socket.socket()
post = 8000
c.connect(("127.0.0.1",post))
while True:
    mgs = input(">>>>:")

    c.send(mgs.encode("utf-8"))
    data = c.recv(1024)
    print("recv",data.decode())


c.close()
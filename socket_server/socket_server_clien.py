#!/usr/bin/env python
# -*- coding:UTF-8 -*-

import socket

clien = socket.socket()


clien.connect(("127.0.0.1",8000))

while True:
    data = input(">>:").strip()

    clien.send(data.encode("utf-8"))

    data = clien.recv(1024)
    print(data)







#!/usr/bin/env python
# -*- coding:UTF-8 -*-
import socket
import os
server = socket.socket()

server.bind(("localhost",6969))
server.listen()
while True:
    conn , addr = server.accept()
    while True:

        data = conn.recv(10240000)
        if not  data:
            print("断开.......")
            break
        print("server recv:",data)
        data = data.decode()
        res = os.popen(data).read()

        conn.send(res.encode("utf-8"))

server.close()

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
        data   = conn.recv(1024)
        if not data:
            print("客户端已经断开")
            break
        filename = data.decode()
        print(filename)
        if os.path.isfile(filename):

            f = open(filename,"rb")
            file_size = os.stat(filename).st_size
            conn.send(str(file_size).encode("utf-8"))
            conn.recv(1024)
            for line in f:
                conn.send(line)

            f.close()

        print("发送完毕！")

server.close()







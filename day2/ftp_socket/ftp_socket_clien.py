#!/usr/bin/env python
# -*- coding:UTF-8 -*-
import socket

clien = socket.socket()

clien.connect(("localhost",6969))

while True:
    data = input(">>:").split()

    if len(data) == 0:
        continue

    if data[0]=="get":
        clien.send(data[1].encode("utf-8"))

    file_size = clien.recv(1024)
    file_size = file_size.decode()
    print(file_size)
    file_size = int(file_size)
    clien.send("收到总字节".encode("utf-8"))
    print(file_size)
    #print(int (file_size.decode()))
    f = open("new","wb")
    while file_size:
        str = clien.recv(1024)
        file_size = file_size -len(str)
        f.write(str)


    f.close()


clien.close()



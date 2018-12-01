#!/usr/bin/env python
# -*- coding:UTF-8 -*-
import socket
import queue
import select

server = socket.socket()
server.bind(("localhost",8000))
server.listen()
server.setblocking(False)
inputs = [server,]
outputs=[]
msg = {}
while True:
    readable , writeable ,exeptional = select.select(inputs,outputs,inputs)

    for r in readable:
        if r is server:
            print("新连接")
            conn ,adds = server.accept()
            conn.setblocking(False)
            inputs.append(conn)
            msg[conn] = queue.Queue()
        else:
            data = r.recv(1024)
            print("数据",data)
            msg[r].put(data)
            outputs.append(r)


    for w in writeable:
        data = msg[w].get()
        w.send(data)
        outputs.remove(w)

    for e in exeptional:
        if e in outputs:
            outputs.remove(e)

        inputs.remove(e)

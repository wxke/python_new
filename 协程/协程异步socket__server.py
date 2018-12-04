#!/usr/bin/env python
# -*- coding:UTF-8 -*-


import socket,time
from gevent import monkey,socket
import gevent
monkey.patch_all()


def server(post):
    s = socket.socket()
    s.bind(("0.0.0.0",post))
    s.listen(5)
    while True:
        conn , addr = s.accept()
        gevent.spawn (request,conn)



def request(conn):
    try:
        data = conn.recv(1024)
        print("recv",data)
        conn.send(data)
        if not data:
            conn.shutdown(socket.SHUT_WR)
    except Exception as e:
        print(e)
    finally:
        conn.close()



if __name__ == '__main__':
    server(8000)

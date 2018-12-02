#!/usr/bin/env python
# -*- coding:UTF-8 -*-

import socketserver

class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        while True:
            try:
                self.data = self.request.recv(1024).strip()

                print("{} write".format(self.client_address[0]))
                print(self.data)

                self.request.send(self.data.upper())
            except ConnectionResetError as e:
                print("出现错误",e)
                break



if __name__ =='__main__':
    HOST , PORT = 'localhost', 9999
    server =socketserver.TCPServer((HOST,PORT),MyTCPHandler)
    server.serve_forever()




#!/usr/bin/env python

import socket
import json



class connection_server(object):
    def __init__(self):
        self.host = "192.168.1.10"
        self.port = 8007
    def client_config(self):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect((self.host,self.port))
        mark = s.recv(1024)
        sgin = json.loads(mark)
        s.close()
        return sgin
    def send_data(self,data):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect((self.host,self.port))
        mark = s.send(data)
        s.close()


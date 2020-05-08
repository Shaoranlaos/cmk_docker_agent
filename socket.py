#!/usr/bin/env python

import socket
import os
import sys
import subprocess


HOST = '0.0.0.0'
PORT = 6556

class stdout_():

    def __init__(self, sock_resp):
        self.sock_resp = sock_resp

    def write(self, mes):
        self.sock_resp.send(mes)


srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Start server")

srv.bind((HOST, PORT))
srv.listen(0)


while 1:
    sock_resp, addr_resp = srv.accept()
    print 'Connected by', addr_resp

    output = sock_resp.makefile('w',0)
    p = subprocess.Popen('check_mk_agent',stdout=output)
    output, errors = p.communicate()
    sock_resp.close()


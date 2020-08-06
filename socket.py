#!/usr/bin/env python

import socket
import os
import subprocess
from _thread import *

ServerSocket = socket.socket()
host = '0.0.0.0'
port = 6556
ThreadCount = 0
try:
    ServerSocket.bind((host, port))
except socket.error as e:
    print(str(e))

print('Waitiing for a Connection..')
ServerSocket.listen(5)


def threaded_client(connection):
    result = subprocess.check_output(['check_mk_agent'])
    connection.sendall(str.encode(result.stdout.decode('utf-8')))
    connection.close()

while True:
    Client, address = ServerSocket.accept()
    print('Connected to: ' + address[0] + ':' + str(address[1]))
    start_new_thread(threaded_client, (Client, ))
    ThreadCount += 1
    print('Thread Number: ' + str(ThreadCount))
ServerSocket.close()

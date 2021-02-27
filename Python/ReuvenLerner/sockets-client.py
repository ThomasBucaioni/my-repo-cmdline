#!/usr/bin/env python3

import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
host = socket.gethostname()                           
port = 9999
s.connect((host, port))                               

s.send('say hello'.encode())
msg = s.recv(1024).decode()
print(msg)

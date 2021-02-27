#!/usr/bin/env python3

import socket                                         # (1)
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # (2)

host = socket.gethostname()                           # (3)
port = 9999                                           
serversocket.bind((host, port))                       # (4)

serversocket.listen()
print("Ready to accept connection")

clientsocket,addr = serversocket.accept()             # (5)

actions = {
    'say' : lambda word: word,
    'increment' : lambda x: str(int(x) + 1)
}

while True:
    client_message = clientsocket.recv(1024).decode() # (6)
    print(f"client_message = '{client_message.rstrip()}'")
    
    if not client_message:                            # (7)
        break
    
    # (8)
    clientsocket.send(f"Got your message '{client_message.rstrip()}'".encode())
    
# (9)
clientsocket.close()

import socket

message = "Hello, World\n"

# TCP
t = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
destIPAddr = "localhost"
destIPPort = 12346

t.connect((destIPAddr, destIPPort)) # Connection
t.send(message.encode()) # Emission
t.close()

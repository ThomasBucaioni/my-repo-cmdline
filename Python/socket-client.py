import socket

# Datagram (UDP)
s = socket.socket (socket.AF_INET, socket.SOCK_DGRAM)

destIPAddr  = "localhost"
destPort    = 12345
message = "Hello, World\n"

s.sendto(message.encode(), (destIPAddr, destPort))
s.close()

# wait 
import time
time.sleep(5)

# TCP
t = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
destIPAddr = "localhost"
destIPPort = 12346

t.connect((destIPAddr, destIPPort)) # Connection
t.send(message.encode()) # Emission
t.close()

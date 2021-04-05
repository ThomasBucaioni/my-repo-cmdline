import socket

# Datagram (UDP)
s = socket.socket (socket.AF_INET, socket.SOCK_DGRAM)
myAddress = ''         # Écouter sur toutes les interfaces réseau
myPort    = 12345         # Port sur lequel écouter
s.bind((myAddress, myPort))
message, sourceAddr = s.recvfrom(1024)
print(f"Message from the client : {message}")
s.close()

# TCP
t = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
myAddress = ''
myPort = 12346

t.bind((myAddress, myPort))
t.listen(5) # Max clients
sData, senderAddress = t.accept() # Listen
message = sData.recv(1024) # Reception
sData.close()

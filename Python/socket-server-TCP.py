import socket

# TCP
t = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
myAddress = ''
myPort = 12346

t.bind((myAddress, myPort))
t.listen(5) # Max clients
sData, senderAddress = t.accept() # Listen
message = sData.recv(1024) # Reception
print(f"Message from the client : {message}")
sData.close()

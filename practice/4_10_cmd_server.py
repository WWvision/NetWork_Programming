from socket import *
import sys

port = 2500
BUFSIZE = 1024

if len(sys.argv) > 1:
    port = int(sys.argv[1])
    
sock = socket(AF_INET, SOCK_STREAM)
sock.bind(('', port))
sock.listen(1)
print("Waiting for connection...")
client_server, addr = sock.accept()
print("Connected by", addr)

while True:
    data = client_server.recv(BUFSIZE)
    if not data:
        break
    print("Received message: ", data.decode())
    client_server.send(data)
    
client_server.send(data)

#Use 4_5_echo_client_exception.py
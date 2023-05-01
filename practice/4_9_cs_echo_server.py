from socket import *

port = 2500
BUFSIZE = 1024

sock = create_server(('',port), family=AF_INET, backlog=1)
conn, addr = sock.accept()
print("Connected By", addr)

while True:
    data = conn.recv(BUFSIZE)
    if not data:
        break
    print("Received message: ", data.decode())
    conn.send(data)
    
conn.close()

#Use 4_5_echo_client_exception.py
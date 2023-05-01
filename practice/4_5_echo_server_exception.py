from socket import *

port = 2500
BUFSIZE = 1024

sock = socket(AF_INET, SOCK_STREAM)
sock.bind(('',port))
print("Wating for connection...")
sock.listen(1)
client_socket, addr = sock.accept()
print("Connected By ", addr)

while True:
    try:
        data = client_socket.recv(BUFSIZE)
    except: 
        break
    else:
        if not data:
            break
        elif data.decode() == 'quit':
            break
        print("Received message: ", data.decode())
        
    try:
        client_socket.send(data)
    except:
        break
    
    
    
client_socket.close()
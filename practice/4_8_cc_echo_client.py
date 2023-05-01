import socket

BUFSIZE = 1024

server_socket = socket.create_connection(('localhost', 2500))

while True:
    msg = input("Message to Send: ")
    server_socket.send(msg.encode())
    data = server_socket.recv(BUFSIZE)
    if not data:
        break
    print("Received message: %s" % data.decode())
    
server_socket.close()

#Use 4_5_echo_server_exception.py
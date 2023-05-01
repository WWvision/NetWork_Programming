import socket

port = int(input("Port No: "))
address = ('localhost', port)
BUFSIZE = 1024

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.connect(address)

while True:
    msg = input("Message to Send: ")
    server_socket.send(msg.encode())
    data = server_socket.recv(BUFSIZE)
    print("Received message:  %s" % data.decode())
    
server_socket.close()
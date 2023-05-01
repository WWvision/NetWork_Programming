from socket import *

server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.connect(('localhost', 3333))

while True:
    msg = input('Number to send(1~10): ')
    if msg == 'q':
        break
    server_socket.send(msg.encode())
    
    print('Received message: ', server_socket.recv(1024).decode())
    
server_socket.close()
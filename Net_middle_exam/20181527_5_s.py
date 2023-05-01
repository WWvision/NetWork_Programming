import socket
import json
from random import *

#Server

port = 7625

    
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('', port))
server_socket.listen(3)
print('[Device1]: Waiting Client Connection...')

while True:
    client_socket, addr = server_socket.accept()
    print('Connection from Client IP:', addr)
    client_socket.send(str(addr[0]).encode())
    recv_data = client_socket.recv(1024)
    msg = recv_data.decode()
    data = 0
    if msg == '1':
        temp = randint(1,50).to_bytes(4, 'big')
        humid = data.to_bytes(4,'big')
        light = data.to_bytes(4,'big')
    elif msg == '2':
        humid = randint(1,100).to_bytes(4, 'big')
        temp = data.to_bytes(4,'big')
        light = data.to_bytes(4,'big')
    elif msg == '3':
        light = randint(1, 150).to_bytes(4, 'big')
        temp = data.to_bytes(4,'big')
        humid = data.to_bytes(4,'big')
        
    
    send_data = temp + humid + light

    client_socket.send(send_data);
    
    
    client_socket.close()
import socket
#import sys
import json
from random import *

#Device1_Server

port = 7625

#if len(sys.argv) > 1:
#    port = int(sys.argv[1])
    
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
    
    if(msg == "Request"):
        temp = randint(0,40)
        humid = randint(0,100)
        light = randint(70, 150)
        dict_data =  { 'check': 1 ,'temp': str(temp), 'humid': str(humid), 'light': str(light)}
    else:
        dict_data =  { 'check': 0 ,'temp': '-1', 'humid': '-1', 'light': '-1'}
        
    json_data = json.dumps(dict_data)
    send_data = json_data.encode()
    client_socket.send(send_data);
    
    
    client_socket.close()
import socket
#import sys
import json
from random import *

#Device2_Server

port = 7626

#if len(sys.argv) > 1:
#    port = int(sys.argv[1])
    
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('', port))
server_socket.listen(3)
print('[Device2]: Waiting Client Connection...')

while True:
    client_socket, addr = server_socket.accept()
    print('Connection from Client IP:', addr)
    client_socket.send(str(addr[0]).encode())
    recv_data = client_socket.recv(1024)
    msg = recv_data.decode()
    
    if(msg == "Request"):
        heart = randint(40,140)
        steps = randint(2000,6000)
        cal = randint(1000, 4000)
        dict_data =  { 'check': 1 ,'heart': str(heart), 'steps': str(steps), 'cal': str(cal)}
    else:
        dict_data =  { 'check': 0 ,'heart': '-1', 'steps': '-1', 'cal': '-1'}
        
    json_data = json.dumps(dict_data)
    send_data = json_data.encode()
    client_socket.send(send_data);
    
    
    client_socket.close()
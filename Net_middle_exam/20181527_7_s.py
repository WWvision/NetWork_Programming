import socket
import random
import struct

port = 9999
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('', port))
server_socket.listen(1)
print('Waiting Client Connection...')

while True: 
    client_socket, addr = server_socket.accept()
    print('Connection from Client IP:', addr)
    client_socket.send(str(addr[0]).encode())
    msg = client_socket.recv(1024).decode()
    
    if msg == 'Hello':
        packed = b''
        #송신자
        sender = random.randint(1, 50000)
        packed += struct.pack('H', sender) 
        #수신자
        receiver = random.randint(1, 50000)
        packed += struct.pack('H', receiver)
        #조도
        Lumi = random.randint(1, 100)
        packed += struct.pack('B', Lumi)
        #온도
        Humi = random.randint(1, 100)
        packed += struct.pack('B', Humi)
        #습도
        Temp = random.randint(1, 100)
        packed += struct.pack('B', Temp)
        #온도
        Air = random.randint(1, 100)
        packed += struct.pack('B', Air)
        #기압
        seq = random.randint(1, 100000)
        packed += struct.pack('I', seq)
        
        client_socket.send(packed)
        
    
    else:
        print('Wrong msg')
   
    client_socket.close()
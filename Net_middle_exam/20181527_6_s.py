import socket
import random

port = 3333
BUFSIZE = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #SOCK_DGRAM: UDP
sock.bind(('', port))

while True:
    data, addr = sock.recvfrom(BUFSIZE) #데이터 받기
    if data.decode() == 'ping':
        while True:
            if random.randint(1, 10) <= 4: #의도적으로 40% 데이터 손실
                print('Pack from {} lost!'.format(addr))
                continue #이뜻은 ack을 client 
            
            sock.sendto('pong'.encode(), addr)
            break
        
from socket import *
import random

BUF_SIZE = 1024
port = 5555

s_sock = socket(AF_INET, SOCK_DGRAM)
s_sock.bind(('',port))
print('Listening...')

while True:
    data, addr = s_sock.recvfrom(BUF_SIZE)
    if random.randint(1, 10) <= 3: #의도적으로 30% 데이터 손실
        print('Pack from {} lost!'.format(addr))
        continue #이뜻은 ack을 client 
    print('Packet is {} from {}'.format(data.decode(), addr))
    
    s_sock.sendto('ack'.encode(), addr)
    
    
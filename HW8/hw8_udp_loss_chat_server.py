from socket import *
import random
import time

port = 3333
BUF_SIZE = 1024

sock = socket(AF_INET, SOCK_DGRAM)
sock.bind(('', port))

while True:
    #메세지 수신 처리 부분
    sock.settimeout(None) #소켓의 블로킹 모드 timeout 설정
    while True:
        data, addr = sock.recvfrom(BUF_SIZE)
        if random.random() <= 0.5:
            continue
        else:
            sock.sendto(b'ack', addr)
            print('<-', data.decode())
            break
        
    #메세지 송신 처리 부분
    msg = input('-> ')
    reTx = 0
    while reTx <= 5:#최대 5회까지 재전송
        resp = str(reTx) + ' ' + msg
        sock.sendto(resp.encode(), addr)
        sock.settimeout(2)
        
        try:
            data, addr = sock.recvfrom(BUF_SIZE)
        except timeout:
            reTx += 1
            continue
        else:
            break
        
    if reTx > 5:
        print('Timeout.')
    
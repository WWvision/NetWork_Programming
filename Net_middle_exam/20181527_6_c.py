from socket import *
import time

port = 3333
BUFSIZE = 1024

sock = socket(AF_INET, SOCK_DGRAM)


while True:
    
    msg = input('ping입력:')
    sock.sendto(msg.encode(), ('localhost', port))
    send_time =  time.time()
    data = 0
    data, addr = sock.recvfrom(BUFSIZE)
    if data.decode() == 'pong':
        recv_time = time.time()
        rtt = recv_time - send_time
        print('Success (RTT: {})'.format(rtt))
    else:
        print('Fail')
    
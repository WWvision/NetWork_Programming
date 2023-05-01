from socket import *

port = 3333
BUFSIZE = 1024

sock = socket(AF_INET, SOCK_DGRAM)
sock.bind(('', port))

while True:
    data, addr = sock.recvfrom(BUFSIZE) #데이터 받기
    print('<- ', data.decode())         #받은 데이터 표시
    resp = input('-> ')                 #데이터 입력
    sock.sendto(resp.encode(), addr)    #입력된 데이터 보내기
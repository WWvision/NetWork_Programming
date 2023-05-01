import socket

port = 2500
BUFSIZE = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #SOCK_DGRAM: UDP
sock.bind(('', port))

while True:
    msg, addr = sock.recvfrom(BUFSIZE) #TCP에서는 UDP와 달리 connect과정을 통해 수신자와 연결 후 통신을 하여 따로 addr 주소를 확인하지 않아도 되는데
    print('Received: ', msg.decode())
    sock.sendto(msg, addr) #UDP는 Client와 connect과정을 안하기 때문에 보낼때 송신자의 정보를 보내야함
    
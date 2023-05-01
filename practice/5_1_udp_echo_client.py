import socket

port = 2500
BUFSIZE = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #UDP

while True:
    msg = input('Enter a message: ')
    if msg == 'q':
        break
    #TCP 송신: send  / 수신: recv
    #UDP 송신: sendto / 수신: recvfrom 
    sock.sendto(msg.encode(), ('localhost', port)) #addr은 튜플 형태로하여 데이터를 보내기
    data, addr = sock.recvfrom(BUFSIZE)
    print('Server says: ', data.decode())
    
sock.close()
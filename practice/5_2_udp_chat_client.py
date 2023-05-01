from socket import *

port = 3333
BUFSIZE = 1024

sock = socket(AF_INET, SOCK_DGRAM)

while True:
    msg = input('-> ')
    sock.sendto(msg.encode(), ('localhost', port))
    
    send_time = time.time()
    data, addr = sock.recvfrom(BUFSIZE)
    print('<- ', data.decode())
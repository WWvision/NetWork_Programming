from socket import *

port = 3333
BUFSIZE = 1024

sock = socket(AF_INET, SOCK_DGRAM)

while True:
    # msg = input('-> ')
    # sock.sendto(msg.encode(), ('localhost', port))
    # data, addr = sock.recvfrom(BUFSIZE)
    # print('<- ', data.decode())
    
    msg = input('Enter the message("send [mboxID] message" or "receive mboxId"):')
    
    if msg == 'quit':
        sock.sendto(msg.encode(), ('localhost', port))
        break
    else:
        sock.sendto(msg.encode(), ('localhost', port))
        data, addr = sock.recvfrom(BUFSIZE)
        print(data.decode())
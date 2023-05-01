from socket import *

port = 3333
BUFSIZE = 1024

sock = socket(AF_INET, SOCK_DGRAM)

while True:
    msg = input('Enter the message("send [mboxID] message" or "receive mboxId"):')
    
    if msg == 'quit':
        sock.sendto(msg.encode(), ('localhost', port))
        break
    else:
        time = 2
        count = 0
        while True:
            sock.sendto(msg.encode(), ('localhost', port))
            print('Packet: Waiting count {} for ack'.format(count))
            sock.settimeout(time)
            try:
                data = sock.recv(BUFSIZE)
            except timeout:
                count += 1
                if count > 3:
                    break
            else:
                print('Response',  data.decode())
                break
        data, addr = sock.recvfrom(BUFSIZE)
        print(data.decode())
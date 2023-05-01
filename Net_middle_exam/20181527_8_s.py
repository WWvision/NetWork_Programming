from socket import *

port = 3333
BUFSIZE = 1024
import random

sock = socket(AF_INET, SOCK_DGRAM)
sock.bind(('', port))
SERVER_DB = {}
while True:
    while True:
        if random.randint(1, 10) <= 1: #의도적으로 10% 데이터 손실
                print('Pack from {} lost!'.format(addr))
                continue #이뜻은 ack을 client 
            
        data, addr = sock.recvfrom(BUFSIZE) #데이터 받기
        sock.sendto('ack'.encode(), addr)
        break
    
    recv_msg = data.decode().split(' ', maxsplit=2)
    #클라이언트로부터 send [mboxId] msg 수신시
    if recv_msg[0] == 'send':
        data_key =  str(recv_msg[1])
        data_value = recv_msg[2]
        
        if data_key in SERVER_DB:
            SERVER_DB[data_key].append(data_value)
        else: 
            SERVER_DB[data_key] = [data_value]
            
        sock.sendto('OK'.encode(), addr)

    #클라이언트로부터 receive [mboxId] 수신시
    elif recv_msg[0] == 'receive':
        if SERVER_DB.get(recv_msg[1]) == None:
            sock.sendto('No messages'.encode(), addr)
        else:
            if len(SERVER_DB.get(recv_msg[1])) != 0:
                send_data = SERVER_DB[recv_msg[1]].pop(0)
            else:
                send_data = 'No messages'
            sock.sendto(send_data.encode(), addr)

    
    elif recv_msg[0] == 'quit':
        print('프로그램을 종료합니다')
        break
    
    else:
        sock.sendto('Error wrong format'.encode(), addr)
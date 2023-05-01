from socket import *

port = 3333
BUFSIZE = 1024

sock = socket(AF_INET, SOCK_DGRAM)
sock.bind(('', port))
SERVER_DB = {}
while True:
    data, addr = sock.recvfrom(BUFSIZE) #데이터 받기
    # print('<- ', data.decode())         #받은 데이터 표시
    # resp = input('-> ')                 #데이터 입력
    # sock.sendto(resp.encode(), addr)    #입력된 데이터 보내기
    
    recv_msg = data.decode().split(' ', maxsplit=2)
    #클라이언트로부터 send [mboxId] msg 수신시
    if recv_msg[0] == 'send':
        data_key =  str(recv_msg[1])
        data_value = recv_msg[2]
        # i = 3
        # data_value = recv_msg[2]
        # if len(recv_msg) > 3:
        #     for i in len(recv_msg):
        #         data_value += ' ' + recv_msg[i]
        
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
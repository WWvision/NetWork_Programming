import socket
import json
from time import ctime
import sys

port1 = 7625
port2 = 7626
# if len(sys.argv) > 1 and len(sys.argv[1]) == 4:#device1 port
#     port1 = int(sys.argv[1])
# if len(sys.argv) > 1 and len(sys.argv[2]) == 4:
#     port1 = int(sys.argv[1])


def socket_data(ip, port, msg):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    addr = (ip,port)
    server_socket.connect(addr)
    receive_msg = server_socket.recv(1024)
    print('Connection from Sercer IP: ', receive_msg.decode())
    server_socket.send(msg.encode())
    return server_socket
    
def inp_help():    
    print("-----------------------------------------------------------------------------------------------------------------")
    print("-----------------------------------------------------------------------------------------------------------------")
    print('--    안녕하세요. IoT디바이스 센서 출력 프로그램에 오신걸 환영합니다.                                          --')
    print("--    '1'입력: [Device 1]는 온도,습도,조도  / '2'입력: [Device 2]는 심박수,걸음수,소모칼로리 데이터를 수집하고 --")
    print("--    종료를 원하시면 'q'입력 또는 'quit'을 입력하시면 프로그램이 종료됩니다.                                  --")    
    print("--    설명을 다시 보시려면 'h' 나 'help'를 입력해주세요.                                                       --")
    print("-----------------------------------------------------------------------------------------------------------------")
    print("-----------------------------------------------------------------------------------------------------------------\n\n")
    
inp_help()


while True:
    inp_data = input('값을 입력하세요: ')
    
    # [Device 1]
    if (inp_data == '1'):
        device1_socket = socket_data('localhost', port1, 'Request')
        recv_msg = device1_socket.recv(1024).decode()
        recv_data = json.loads(recv_msg)
        if (recv_data['check'] == 1): # [Device1] 데이터가 정상적으로 받아왔으면 값 출력
            # { 'check': 1 ,'temp': temp, 'humid': humid, 'light': light}
            device1_data = ctime() + ': Device1: Temp=' + recv_data['temp'] + ', Humid=' + recv_data['humid'] + ', lilum=' + recv_data['light']
            data_txt = open('data.txt', 'a')
            print(ctime(), ': Device1: ', 'data.txt로 데이터가 정상적으로 저장되었습니다.')
            print(device1_data, file=data_txt)
            
        else: # [Device1] 서버에서 데이터를 정상적으로 처리 못함
            print(ctime(), ': Device1: ', 'Error! - 서버에서 데이터를 생성하지 못했습니다 다시 시도해주세요.')
           
        device1_socket.close() #[Device 1] 데이터 통신 종료 
            
    # [Device 2]
    elif (inp_data == '2'):
        device2_socket = socket_data('localhost', port2, 'Request')
        recv_msg = device2_socket.recv(1024).decode()
        recv_data = json.loads(recv_msg)
        if (recv_data['check'] == 1): # [Device2] 데이터가 정상적으로 받아왔으면 값 출력
            # { 'check': 1 ,'heart': heart, 'steps': steps, 'cal': cal}
            device2_data = ctime() + ': Device2: Heartbeat=' + recv_data['heart'] + ', Steps=' + recv_data['steps'] + ', Cal=' + recv_data['cal']
            data_txt = open('data.txt', 'a')
            print(ctime(), ': Device2: ', 'data.txt로 데이터가 정상적으로 저장되었습니다.')
            print(device2_data, file=data_txt)
            
        else: # [Device2] 서버에서 데이터를 정상적으로 처리 못함
            print(ctime(), ': Device2: ', 'Error! - 서버에서 데이터를 생성하지 못했습니다 다시 시도해주세요.')
            
        device2_socket.close()#[Device 2] 데이터 통신 종료
            
    # [Finish Programm]
    elif (inp_data == 'q') or (inp_data == 'quit'):
        device1_socket = socket_data('localhost', port1, 'quit')
        device2_socket = socket_data('localhost', port2, 'quit')
        device1_socket.close()#[Device 1] 데이터 통신 종료
        device2_socket.close()#[Device 2] 데이터 통신 종료
        print('프로그램이 정상적으로 종료되었습니다.')
        break;
    # [Explain Programm]
    elif (inp_data == 'h') or (inp_data == 'help'):
        inp_help()
    # [Error]
    else: 
        print('지정되지 않은 값입니다. 다시입력해주세요')
    
    
from socket import *
import sys

BUF_SIZE = 1024
LENGTH = 4  # Big Endian 방식으로 전송하기 위함 OxOaOaOaOa 
# 파일크기 : 4바이트

sock = socket(AF_INET, SOCK_STREAM)
sock.connect(('localhost', 7777))

sock.send(b'Hello') # 'Hello' 메세지 전송

msg = sock.recv(BUF_SIZE) #'Filename' 메세지 수신
if not msg:
    sock.close()
    sys.exit()
elif msg != b'Filename': #서버로부터 받은 메세지가 'Filename'이 아닌 경우
    print('server: ', msg.decode())#서버에서보낸 에러메세지 처리
    sock.close()
    sys.exit()
else:  #정상적인 경우
    print('server:', msg.decode())
    
filename = input('Enter a filename: ')
sock.send(filename.encode()) #입력받은 파일 이름 전송

msg = sock.recv(BUF_SIZE) #서버로부터 받은 파일이름에 대한 결과 메세지
if not msg:
    sock.close()
    sys.exit()
elif msg == b'Nofile':  #파일이 서버에 없는 경우
    print('server: ', msg.decode())
    sock.close()
    sys.exit()
else:   #정상적인 경우
    rx_size = len(msg) #데이터 크기 ?????
    data = msg
    while rx_size < LENGTH: # 4바이트의 길이씩 데이터를 받는 과정
        msg = sock.recv(BUF_SIZE)
        if not msg:
            sock.close()
            sys.exit() #끝냄
        data = data + msg
        rx_size += len(msg) #받은 데이터를 
    
    if rx_size < LENGTH:
        sock.close()
        sys.exit()
    filesize = int.from_bytes(data, 'big')
    print('server:',filesize)# 4byte
    
rx_size = 0 
f = open(filename, 'wb')    #파일 열기
while rx_size < filesize:   #실제 파일 수신 
    data = sock.recv(BUF_SIZE) #데이터를 받는 과정
    if not data:
        break
    f.write(data)
    rx_size += len(data)
    
if rx_size < filesize:
    sock.close()
    sys.exit()
    
print('Download Complete')
sock.send(b'Bye') # 'Bye' 메세지 전송
f.close()
sock.close()

from socket import *
import os

BUF_SIZE = 1024
LENGTH = 4 
# 파일 크기 : 4바이트 

sock = socket(AF_INET, SOCK_STREAM)
sock.bind(('', 7777))
sock.listen(10)
print('File Server is running...')

while True:
    conn, addr = sock.accept()
    msg = conn.recv(BUF_SIZE) #'Hello' 메세지 수신
    if not msg: #문제가 생기면
        conn.close() #해당 소켓만 닫고
        continue #다른 클라이언트와 통신하기 위해 다음 준비
    elif msg != b'Hello': #클라로부터 수신받은 데이터가 Hello가 아니면
        print('Client : ', addr, msg.decode())
        conn.close()
        continue
    else: #정상적인 경우
        print('Client: ', addr, msg.decode())
        
    # 'Filename' 메세지 전송
    conn.send(b'Filename')
    
    #파일 이름 수신
    msg = conn.recv(BUF_SIZE) #클라이언트가 입력한 파일명
    if not msg:
        conn.close()
        continue
    filename = msg.decode()
    print('Client:', addr, filename)
    
    try:
        filesize = os.path.getsize(filename) #서버에서 가진 파일이름이 없는 경우
    except: #클라이언트에게 파일이 없다고 메세지 전송
        conn.send(b'Nofile') 
        conn.close()
        continue
    else:   #파일 크기 전송
        fs_binary = filesize.to_bytes(LENGTH, 'big')
        conn.send(fs_binary)
        
    f = open(filename, 'rb') #파일 열기
    data = f.read()          #파일 읽기
    conn.sendall(data)       #파일 전송
    
    msg = conn.recv(BUF_SIZE) #'Bye' 메세지 수신하면
    if not msg: #아무메세지를 받지 않는다면 
        pass #아무것도 안한다는 뜻
    else:
        print('Client:', addr, msg.decode()) #정상적으로 메세지가 수신하면 수신한 메세지 출력
        
    # 통신이 끝나면 반드시 종료
    f.close() 
    conn.close()
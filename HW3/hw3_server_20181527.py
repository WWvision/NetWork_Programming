import socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('', 7253))
s.listen(2)

while True:
    client, addr = s.accept()
    print('Connection from ', addr);
    client.send(b'Hello ' + addr[0].encode())

    #이름을 클라이언트로부터 수신한 후 출력 - 문자열 송수신 방식   
    msg_name = client.recv(1024)
    print(msg_name.decode())
    #학번을 클라이언트로 전송 - 정수 송수신 방식
    msg_StudentId = 20181527
    client.send(msg_StudentId.to_bytes(8, 'big')) 
    
    client.close()
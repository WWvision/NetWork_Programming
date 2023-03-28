import socket

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
addr = ('localhost', 7253);
sock.connect(addr)
msg_name = sock.recv(1024)
print(msg_name.decode())

#이름을 문자열로 서버에 전송 - 문자열 송수신 방식
sock.send(b'SeungJu Kim');

#서버로부터 학번을 수신 후 출력 - 정수 송수신 방식
msg_id = sock.recv(1024)
msg_id = int.from_bytes(msg_id,'big')
print(msg_id)

sock.close()

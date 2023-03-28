import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = ('localhost',7625)
server_socket.connect(addr)
receive_msg = server_socket.recv(1024)
print('Connection from Sercer IP: ', receive_msg.decode())
#
while True:
    inp_msg = input('표현식을 입력하세요 (ex. a + b, 공백으로 구분): ')
    if inp_msg=='q' and inp_msg=='quit':
        break
    server_socket.send(inp_msg.encode())
    print('Received message:', server_socket.recv(1024).decode())
server_socket.close()
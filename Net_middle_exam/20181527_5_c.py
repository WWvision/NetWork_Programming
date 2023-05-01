import socket
import struct
port = 7625



while True:
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    addr = ('localhost',7625)
    server_socket.connect(addr)
    receive_msg = server_socket.recv(1024)
    print('Connection from Sercer IP: ', receive_msg.decode())
    inp_data = input('값을 입력하세요: ')
    server_socket.send(inp_data.encode())
    data = server_socket.recv(1024)

    result = struct.unpack('>iii', data) 
    print('Temp=' + str(result[0]) + ', Humid=' + str(result[1]) + ', Lumi=' + str(result[2]))
    server_socket.close()
   
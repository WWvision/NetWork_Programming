import socket
import struct


#
while True:
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    addr = ('localhost',9999)
    server_socket.connect(addr)
    receive_msg = server_socket.recv(1024)
    print('Connection from Sercer IP: ', receive_msg.decode())
    inp_msg = input('입력하세요(Hello):')
    if inp_msg=='q' and inp_msg=='quit':
        break
    server_socket.send(inp_msg.encode())
    packed = server_socket.recv(1024)
    
    try:
        unpacked = struct.unpack('!HHBBBBI', packed)
        print('Sender:{}, Receiver:{}, Lumi:{}, Huni:{}, Temp:{}, Air:{}, Seq:{}'.format(unpacked[0],unpacked[1],unpacked[2],unpacked[3],unpacked[4],unpacked[5],unpacked[6]))
    except:
        print("Error Wrong format") 
    server_socket.close()
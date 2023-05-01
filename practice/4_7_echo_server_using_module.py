import MyTCPServer as my
port = 2500
BUFSIZE = 1024
sock = my.TCPServer(port)
conn, addr = sock.Accept()
print('Connected By', addr)

while True:
    data = conn.recv(BUFSIZE)
    if not data:
        break
    print("Received Message: ", data.decode())
    conn.send(data)
    
conn.close()

#Use 4_5_echo_client_exception.py
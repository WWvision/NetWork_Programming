from socket import *
port = 2500
BUFSIZE = 1024
sock = socket(AF_INET, SOCK_STREAM)
sock.bind(('', port))
sock.listen(1)
print('Waiting for connection...')
conn, addr = sock.accept()#원래 addr은 (remotehost, remoteport)였음
print('Conneted By ', addr)
while True:
    data = conn.recv(BUFSIZE)
    if not data: 
        break
    print("Received Message: ", data.decode())
    conn.send(data)
    
conn.close()
sock.close()

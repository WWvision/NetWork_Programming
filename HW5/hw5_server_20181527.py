import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('', 80))
server_socket.listen(10)
print('Waiting Client Connection...')

while True: 
    client_socket, addr = server_socket.accept()
    print('Connection from Client IP:', addr)
    recv_data = client_socket.recv(1024)
    msg = recv_data.decode()
    req = msg.split('\r\n')#0번째 인덱스는 GET /index.html HTTP/1.1 
    comm = req[0].split(' ')# [GET, /index.html, HTTP1.1]
    file_name = comm[1][1:]#원하는 파일명
    if(file_name == 'index.html'):
        f = open('./index.html', 'r', encoding='utf-8')
        mimeType = 'text/html'
        success = True
    elif(file_name == 'iot.png'):
        f = open('./iot-1.png', 'rb')
        mimeType = 'image/png'
        success = True
    elif(file_name == 'favicon.ico'):
        f = open('./favicon.ico', 'rb')
        mimeType = 'image/x-icon'
        success = True
    else: 
        #send_data = "Error 404!: Not Found"
        success = False
        
    if(success):
        #header
        client_socket.send(b'HTTP/1.1 200 OK\r\n')
        client_socket.send(b'Content-Type: ' + mimeType.encode() + b'\r\n')
        client_socket.send(b'\r\n')
        #body 
        send_data = f.read()
        if(mimeType == 'text/html'):
            client_socket.send(send_data.encode('euc-kr'))
        else:            
            client_socket.send(send_data)
    else:
        #header
        client_socket.send(b'HTTP/1.1 Not Found\r\n')
        client_socket.send(b'\r\n')
        #body
        client_socket.send(b'<HTML><HEAD><TITLE>Not Found</TITLE></HEAD>')
        client_socket.send(b'<BODY>Not Found</BODY></HTML>')        
    
    client_socket.close()  


    

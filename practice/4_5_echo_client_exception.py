import socket

port = int(input("Port No: "))
addr = ('localhost', port)
BUFSIZE = 1024
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.connect(addr)

while True:
    msg = input("Message to send: ")
    try:
        bytesSend = server_socket.send(msg.encode())
    except:
        print("Connection Closed")
        break
    else:
        print("{} bytes send".format(bytesSend))
    
    try:
        data = server_socket.recv(BUFSIZE)
    except:
        print("Connection Closed")
        break
    else:
        if not data:
            break
        print("Receive message: %s" % data.decode())
        
server_socket.close()
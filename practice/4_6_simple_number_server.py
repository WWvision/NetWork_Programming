from socket import *

table = {
    '1': 'one',
    '2': 'two',
    '3': 'three',
    '4': 'four',
    '5': 'five',
    '6': 'six',
    '7': 'seven',
    '8': 'eight',
    '9': 'nine',
    '10': 'ten'
}

sock = socket(AF_INET, SOCK_STREAM)
sock.bind(('', 3333))
sock.listen(5)
print("Waiting for Connection...")

while True:
    client_socket, addr = sock.accept()
    print("Connection from", addr)
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        try:
            rsp = table[data.decode()]
        except:
            client_socket.send(b'Try again')
        else:
            client_socket.send(rsp.encode())
            
    client_socket.close()
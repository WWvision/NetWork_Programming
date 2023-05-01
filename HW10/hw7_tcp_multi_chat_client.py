from socket import *
import threading

def recvTask(sock):
    while True:
        msg = sock.recv(1024)
        print(msg.decode())
        

sock = socket(AF_INET, SOCK_STREAM)
sock.connect(('localhost', 5556))

my_id  = input('ID를 입력하세요: ')
sock.send(('[' + my_id + ']').encode())

th = threading.Thread(target=recvTask, args=(sock,))
th.daemon = True
th.start()

while True:
    msg = '[' + my_id + ']' + input()
    sock.send(msg.encode())
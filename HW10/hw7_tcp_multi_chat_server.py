from socket import *
import time
import threading

clients = []
port = 5556

def sendTask(conn, addr):
    while True:
        data = conn.recv(1024)
        
        if 'quit' in data.decode():
            if conn in clients:
                print(addr, 'exited')
                clients.remove(conn)
                continue
        else:
            print(time.asctime() + str(addr) + ':' + data.decode())
            for client in clients:
                if client != conn:
                    client.send(data)
                    
sock = socket(AF_INET, SOCK_STREAM)
sock.bind(('', port))
sock.listen(5)
print("Waiting for Connection...")

while True:
    conn, addr = sock.accept()
    
    if conn not in clients:
        print('new client', addr)
        clients.append(conn)
        
    th = threading.Thread(target=sendTask, args=(conn, addr,))
    th.start()
    
sock.close()                    
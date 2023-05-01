from socket import *
import argparse

sock = socket(AF_INET, SOCK_STREAM)

parser = argparse.ArgumentParser()
parser.add_argument('-s', default='localhost')
parser.add_argument('-p', type=int, default=2500)
args = parser.parse_args()

sock.connect((args.s, args.p))
print('Connection to ', args.s, args.p)
#args.s : IP
#args.p : Port

while True:
    msg = input("Message to send:  ")
    if msg == 'q':
        break
    sock.send(msg.encode())
    data = sock.recv(1024)
    if not data:
        break
    print("Received message: ", data.decode())
    
sock.close()

#Use 4_11_cmd_server.py

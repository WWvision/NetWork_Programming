import socket
import time

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.bind(('', 9999))
client_socket.listen(5)
print('Waiting for connection...')

while True:
    client, addr = client_socket.accept()
    print('Connection from ', addr)
    client.send(time.ctime(time.time()).encode())#시간함수
    #time.time() : UTC기준 1970년 1월 1일 0시 0분 0초부터의 경과시간을 나타냄 >> 1583368987.3660107
    #time.ctime() : 초 단위의 시간을 문자열로 변환하는 함수 >> Thu Mar 4 09:43:07 2021
    client.close()
import socket
import binascii 
ip = '220.69.189.125'
port = 443

#A
hostname = socket.gethostbyaddr(ip)
print(hostname[0])
#B
protocol = socket.getservbyport(port)
print(protocol)
#C
hostname = socket.gethostbyaddr(ip)
url = str(socket.getservbyport(port)) + '://' + hostname[0]
print(url)
#D
for string_address in [ip]:
    packed = socket.inet_aton(string_address) 
    print ('Packed  :', binascii.hexlify(packed)) 



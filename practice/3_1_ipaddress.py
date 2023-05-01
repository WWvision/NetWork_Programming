import ipaddress
addr4 = ipaddress.ip_address('192.9.2.1')
print(addr4)
addr6 = ipaddress.ip_address('2001:A8::1')
print(addr6)

print(addr4.version)
print(addr6.version)
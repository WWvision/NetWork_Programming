import ipaddress
net = ipaddress.ip_network('114.71.220.0/24')
print(net)

print(net.with_netmask)
print(net.num_addresses)
print(net.netmask)
print(net.hostmask)
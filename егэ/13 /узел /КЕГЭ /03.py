from ipaddress import *
k = 0
for A in range(256):
    ip = ip_address(f'207.0.{A}.167')
    net = ip_network(f'207.0.{A}.167/255.255.255.192', 0)
    if net[0] < ip < net[-1] and all(f'{ip:b}'[:16].count('0') > f'{ip:b}'[16:].count('0') for ip in net):
        k += 1
print(k)

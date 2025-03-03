# задача с открытого курса кабанова (первая)
from ipaddress import *

ip = ip_address("238.237.149.255")

for mask in range(31):
    net = ip_network(f"238.237.149.255/{mask}", 0)
    if net[0] < ip < net[-1]:
        print(net)
# ans - 22

from ipaddress import *
k = 0
net = ip_network("96.233.201.87/255.255.248.0", 0)

for ip in net:
    if "10001" in f"{ip:b}": k += 1
print(k)

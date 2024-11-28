from ipaddress import *
net = ip_network('172.30.0.0/255.254.0.0')
c = 0
for i in net:
    if bin(int(i))[2:].count('1') % 12 != 0:
        c += 1
print(c)

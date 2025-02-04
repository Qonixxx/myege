'''
В терминологии сетей TCP/IP маской сети называют двоичное число, которое показывает, какая часть IP-адреса узла сети относится к адресу сети, 
а какая – к адресу узла в этой сети. Адрес сети получается в результате применения поразрядной конъюнкции к заданному адресу узла и его маске.

Широковещательным адресом называется специализированный адрес, в котором на месте нулей в маске стоят единицы.

Сеть задана IP-адресом одного из входящих в неё узлов 218.194.82.148 и сетевой маской 255.255.255.192.

Найдите наибольший IP-адрес в данной сети, который может быть назначен компьютеру.
'''

from ipaddress import *

net = ip_network("218.194.82.148/255.255.255.192", 0)
print(net[-2])

# нулевой адрес (0) - адрес сети
# последний адрес (-1) - широковещательный
# с (1) по (-2) - предназначены компам

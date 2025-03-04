from math import *

for k in range(1, 1000):
    kod = 26 + 26
    char = ceil(log2(kod))
    pas = ceil(char * 7 / 8)
    user = pas + 12
    if user * k <= 2 * 1024: print(k)

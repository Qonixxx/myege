from itertools import product

def ch1(x): return x not in "035"
def ch2(x): return x not in "0246"

k = 0
for a in product("0123456", repeat = 7):
    if ch1(a[0]) and ch2(a[-1]) and a.count("0") <= 1:
        k += 1
print(k)

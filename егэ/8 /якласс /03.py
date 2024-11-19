from itertools import product
k = 0

for x in product("0123456", repeat = 5):
    s = "".join(x)
    sc = s
    sc = sc.replace("2", "0").replace("4", "0").replace("6", "0")
    sc = sc.replace("3", "1").replace("5", "1")
    if len(s) == len(set(s)) and int(s[0]) % 2 != 0 and "11" not in sc and "00" not in sc:
        k += 1
print(k)
# ans - 72

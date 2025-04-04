from itertools import *
k = 0
for x in permutations("0123456789ABC", 5):
    s = "".join(x)
    s = s.replace("2", "0").replace("4", "0").replace("6", "0").replace("8","0")
    s = s.replace("A", "0").replace("C", "0")
    s = s.replace("3", "1").replace("5", "1").replace("7", "1").replace("9", "1")
    s = s.replace("B", "1")
    if "11" not in s and "00" not in s: k += 1
print(k)

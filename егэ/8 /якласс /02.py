from itertools import permutations
k = 0

for x in permutations("ФУНКЦИЯ"):
    s = "".join(x)
    if s[0] != "Я" and "ЯК" not in s and "ЯН" not in s:
        k += 1
print(k)
# ans - 3120

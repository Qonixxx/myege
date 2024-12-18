from sys import *
setrecursionlimit(10000)

def F(n):
    if n == 1:
        return 1
    if n > 1:
        return n - 1 + F(n - 1)

result = F(2024) / F(2022)
print(result)

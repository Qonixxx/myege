# 16-е (увеличение глубины)
from sys import *
setrecursionlimit(10000)

def f(n): return f((n + 2024) // 2025) + 1 if n > 2025 else 1
print(f(2025 ** 2025)) # ans = 2025

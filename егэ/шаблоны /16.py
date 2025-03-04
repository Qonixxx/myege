# 16-е (увеличение глубины)
from sys import *
setrecursionlimit(10000)

def f(n): return f((n + 2024) // 2025) + 1 if n > 2025 else 1
print(f(2025 ** 2025)) # ans = 2025

# ----------------------------------------------------------------------------

# 16-е (кэширование)
from functools import *
@lru_cache(None)

def F(n): return n if n < 5 else 2 * n * F(n - 4)

for i in range(5, 14000): F(i)
print((F(13766) - 9 * F(13762)) // F(13758))

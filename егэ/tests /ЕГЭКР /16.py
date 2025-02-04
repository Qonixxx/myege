from functools import *
@lru_cache(None)

def F(n): return n if n < 5 else 2 * n * F(n - 4)

for i in range(5, 14000): F(i)
print((F(13766) - 9 * F(13762)) // F(13758))

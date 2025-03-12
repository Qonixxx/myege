def f(n):
    if n <= 8: return n
    if n > 8 and n % 2 == 0: return 7 + n * f(n - 2)
    if n > 8 and n % 2 != 0: return 3 * n * f(n - 1)
print((f(31) / 11) + (f(27) / 6))

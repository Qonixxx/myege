def f(s, e):
    if s < e: return 0
    if s == e: return 1
    return f(s - 1, e) + f(s // 2, e)
print(f(30, 12) * f(12, 1)) # 376

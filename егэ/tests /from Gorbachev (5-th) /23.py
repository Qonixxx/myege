def f(s, e, k):
    if s < e: return 0
    if s == e: return 1
    if k < 2: return f(s - 2, e, k) + f(s - 3, e, k + 1) + f(s // 2, e, k)
    else: return f(s - 2, e, k) + f(s // 2, e, k)
print(f(176, 23, 0))

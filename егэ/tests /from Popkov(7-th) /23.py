def f(st, e, s):
    if st > e + 3 or "AAA" in s: return 0
    if st == e and "AAA" not in s: return 1
    return f(st - 1, e, s + "A") + f(st + 5, e, s + "B") + f(st * 2, e, s + "C")
print(f(5, 34, ""))

'''
return f(st - 1, e, s + "A") + f(st + 5, e, s + "B") + f(st * 2, e, s + "C")
print(f(5, 34, ""))
'''

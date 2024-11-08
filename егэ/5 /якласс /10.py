for n in range(2, 10000000):
    r = n
    if r % 5 == 0: r //= 5
    else: r -= 1
    if r % 7 == 0: r //= 7
    else: r -= 1
    if r == 124: print(n)

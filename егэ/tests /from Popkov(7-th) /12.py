for n in range(0, 1000):
    s = "<" + "9" * 39 + "8" * n + "7" * 18
    while "<9" in s or "<8" in s or "<7"  in s:
        s = s.replace("<9", "88<", 1)
        s = s.replace("<8", "8<", 1)
        s = s.replace("<7", "9<", 1)
    s = s.replace("<", "")
    sm = sum(map(int, s))
    if str(sm) == str(sm)[::-1]:
        print(n)
        break

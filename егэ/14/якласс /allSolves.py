def cntToBase(x, base, target):
    cnt = 0
    while x:
        if x % base == target:
            cnt += 1
        x //= base
    return cnt

print(cntToBase((7 * 256 ** 2912 + 5 * 64 ** 1954 - 5 * 8 ** 1991 - 4 * 8 ** 1980 - 2022), 4, 0)) # 5
print(cntToBase((8 * 16 ** 256 + 4 ** 16 * 4 ** 32 + 16 ** 128 - 100011), 5, 0)) # 6
print(cntToBase((5 * 2 ** 2022 + 2 ** 3 * 16 ** 18 + 8 ** 126 - 811), 8, 5)) # 7
print(cntToBase((3 * 4 ** 58 + 3 * 4 ** 13 + 4 ** 15 + 3 * 4 ** 4 + 2 * 4 ** 2 + 1), 4, 0)) # 8


# 4
print(int("650" ,7)) # 329
print(int("475", 9)) # 392
print(int("2324" , 5)) # 339 >= A < C < B

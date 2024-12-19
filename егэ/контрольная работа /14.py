x = 4 * 125 ** 32 - 3 * 25 ** 25 + 4 * 5 ** 13 - 14
count = 0
while x:
    if x % 5 == 4:
        count += 1
    x //= 5
print(count) # 56

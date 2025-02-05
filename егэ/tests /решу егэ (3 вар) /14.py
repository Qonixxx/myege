x = 4 ** 255 + 2 * 255 - 255
s = bin(x)[2:]
print(s.count("1"))

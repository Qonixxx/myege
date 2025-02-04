# первое решение
for x in range(26):
    a = 1 * 25 ** 7 + 1 * 25 ** 6 + 4 * 25 ** 5 + 8 * 25 ** 4 + 8 * 25 ** 3 + 2 * x * 25 ** 2 + 3 * 25 + 3
    if a % 24 == 0:
        print(x, a // 24)

# второе решение
from string import printable

for x in printable[:25]:
    a = int(f"11353{x}12", 25) + int(f"135{x}21", 25)
    if a % 24 == 0:
        print(a // 24)

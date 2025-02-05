from itertools import product
print([m[0] != 'Г' for m in product('ЕГЭ', repeat=5)].count(True))

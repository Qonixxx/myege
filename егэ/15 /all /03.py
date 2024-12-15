print(max(a for a in range(1, 1000) if all((((x & 13 != 0) or (x & a != 0)) <= (x & 13 != 0)) or ((x & a != 0) and (x & 39 == 0)) for x in range(1, 10000))))

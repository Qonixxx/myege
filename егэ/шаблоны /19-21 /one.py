# одна куча
def f(s, m):
    if s >= (): return m % 2 == 0
    if m == 0: return 0
    h = [f( (), m - 1), f( (), m - 1), f((), m - 1), f( () , m - 1)]
    return any(h) if (m - 1) % 2 == 0 else all(h)
    
print("19 ", [s for s in range(st, end) if f(s, 2)])
print("20 ", [s for s in range(st, end) if not f(s, 1) and f(s, 3)])
print("21 ", [s for s in range(st, end) if not f(s, 2) and f(s, 4)])


'------------------------------------------------------------------------------------------------------------------------------------'

'''
одна куча, игра завершается при s >= 33
1) s + 1
2) s + 2
3) s + 3
4) s * 2
'''

def f(s, m):
    if s >= 33: return m % 2 == 0
    if m == 0: return 0
    h = [f(s + 1, m - 1), f(s + 2, m - 1), f(s + 3, m - 1), f(s * 2, m - 1)]
    return any(h) if (m - 1) % 2 == 0 else all(h)
    
print("19 ", [s for s in range(1, 33) if f(s, 2)])
print("20 ", [s for s in range(1, 33) if not f(s, 1) and f(s, 3)])
print("21 ", [s for s in range(1, 33) if not f(s, 2) and f(s, 4)])

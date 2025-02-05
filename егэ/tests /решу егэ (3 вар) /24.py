f = open('24.txt').readline()
while 'AA' in f or 'BB' in f or 'CC' in f:
    f = f.replace('AA','A A')
    f = f.replace('BB','B B')
    f = f.replace('CC','C C')
f = f.split()
print(max(len(x) for x in f))

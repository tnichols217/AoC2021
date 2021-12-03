a = open("1.txt", 'r').read()
b = a.split('\n')

l = 3

c = []

for i in range(len(b)-l+1):
    cur = 0
    for _ in range(l):
        cur+=int(b[i+_])
    print(cur)
    c.append(cur)


d = 0
for i in range(len(c)-1):
    if int(c[i+1]) > int(c[i]):
        d += 1

print(d)

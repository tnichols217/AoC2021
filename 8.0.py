import numpy as np
a = map(lambda a: list(map(lambda b: b.strip().split(), a.split("|"))), open("8.txt", 'r').read().split('\n'))
b = [i[1] for i in a]
c = np.array([[len(j) for j in i] for i in b])
o = 0
for i in [2, 4, 3, 7]:
    o += np.sum([np.sum(np.where(j == i, 1, 0)) for j in c])
print(o)
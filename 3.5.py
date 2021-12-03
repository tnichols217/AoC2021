import numpy as np
from bitstring import BitArray

a = np.array([[int(c) for c in i] for i in open("3.txt", 'r').read().split('\n')])
b = a.copy()

for i in range(len(a[0])):
    c = int(a[:,i].sum() >= len(a)/2)
    d = []
    for j in range(len(a)):
        if a[j][i] != c:
            d.append(j)
    a = np.delete(a, d, axis=0)
    print(len(a), c)

for i in range(len(b[0])):
    c = int(b[:,i].sum() < len(b)/2)
    d = []
    for j in range(len(b)):
        if b[j][i] != c:
            d.append(j)
    b = np.delete(b, d, axis=0)
    if len(b) == 1:
        break
    print(len(b), c)

a = BitArray(a[0].tolist()).uint
b = BitArray(b[0].tolist()).uint

print(a*b)

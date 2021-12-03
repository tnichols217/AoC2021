import numpy as np
from bitstring import BitArray

a = np.array([[int(c) for c in i] for i in open("3.txt", 'r').read().split('\n')]).T
b = len(a[0])
c = [int((i < b/2)) for i in a.sum(axis=1)]
d = BitArray([1 - i for i in c]).uint
e = BitArray(c).uint

print(d*e)

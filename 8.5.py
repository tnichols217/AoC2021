import numpy as np
d = {"a":1, "b":2, "c":3, "d":4, "e":5, "f":6, "g":7}
a = [[[[d[l] for l in k] for k in j.split()] for j in i.split(" | ")] for i in open("8.txt", 'r').read().split('\n')]
d = [[np.sum(np.where(np.array([k for j in i[0] for k in j]) == l, 1, 0)) for l in range(1, 8)] for i in a]
b = [42, 17, 34, 39, 30, 37, 41, 25, 49, 45]
o = [int(''.join([str(b.index(sum([d[i][k-1] for k in j]))) for j in a[i][1]])) for i in range(len(a))]
print(sum(o))

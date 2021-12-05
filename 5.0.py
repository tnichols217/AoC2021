import numpy as np

a = [[[int(k) for k in j.split(',')] for j in i.split(' -> ')] for i in open("5.txt", 'r').read().split('\n')]

b = np.zeros((1000, 1000))

for i in a:
    if i[0][0] == i[1][0]:
        c, d = (i[0][1], i[1][1])
        for j in range(min(c, d), max(c, d)+1):
            b[i[0][0]][j] = 2 if b[i[0][0]][j] > 0 else 1
    if i[0][1] == i[1][1]:
        c, d = (i[0][0], i[1][0])
        for j in range(min(c, d), max(c, d)+1):
            b[j][i[0][1]] = 2 if b[j][i[0][1]] > 0 else 1

b = np.where(b > 1, 1, 0)

print(np.sum(b))
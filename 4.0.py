import numpy as np

a = open("4.txt", 'r').read().split('\n\n')
n = [int(i) for i in a[0].split(',')]
a = [np.array([[int(k) for k in j.split()] for j in i.split('\n')]) for i in a[1:]]

for i in n:
    a = [np.where(j == i, -1, j) for j in a]
    for _ in range(2):
        s = [np.append(j.sum(axis=1), [np.trace(j)]) for j in a]
        for l in range(len(s)):
            for m in s[l]:
                if m == -5:
                    ss = sum([0 if j == -1 else j for j in a[l].flatten()])
                    print(ss * i)
                    exit()
        a = [np.rot90(j) for j in a]

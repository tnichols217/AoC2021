import numpy as np

a = open("4.txt.temp", 'r').read().split('\n\n')
n = [int(i) for i in a[0].split(',')]
a = [np.array([[int(k) for k in j.split()] for j in i.split('\n')]) for i in a[1:]]

for i in n:
    a = [np.where(j == i, -1, j) for j in a]
    s = [np.append(j.sum(axis=1), j.sum(axis=0)) for j in a]
    for l in range(len(s)-1, -1, -1):
        for m in s[l]:
            if m == -5 and len(s) != 1:
                del s[l]
                del a[l]
            elif m == -5 and len(s) == 1:
                ss = sum([0 if j == -1 else j for j in a[0].flatten()])
                print(ss * i)
                exit()

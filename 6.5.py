import numpy as np

a = np.array(list(map(lambda a : int(a) ,open("6.txt", 'r').read().split(','))))
b = np.array([0] * 9)

for i in range(7):
    b[i] = sum(a == i)

for i in range(256):
    b = np.append(b[1:], b[0])
    b[6] += b[8]

print(sum(b))
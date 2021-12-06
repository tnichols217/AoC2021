import numpy as np

a = np.array(list(map(lambda a : int(a) ,open("6.txt", 'r').read().split(','))))

for _ in range(80):
    a -= 1
    b = sum(a == -1)
    a = np.where(a == -1, 6, a)
    print(_, b)
    for __ in range(b):
        a = np.append(a, [8])

print(a)
print(len(a))
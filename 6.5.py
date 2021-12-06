import numpy as np

a = np.array(list(map(lambda a : int(a) ,open("6.txt", 'r').read().split(','))))
b = [sum(a == i) for i in range(9)]

for i in range(256):    
    b[(i + 7) % 9] += b[i % 9]

print(sum(b))
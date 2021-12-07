import numpy as np
a = list(map(int, open("7.txt", 'r').read().split(',')))
dist = np.abs(np.array(a) - int(np.mean(a)))
print(int(sum(dist * (dist + 1))/2))

import numpy as np
a = list(map(int, open("7.txt", 'r').read().split(',')))
print(int(sum(np.abs(np.array(a) - round(np.median(a))))))

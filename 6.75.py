import numpy as np
import time


def trial(iter):
    a = np.array(list(map(lambda a : int(a) ,open("6.txt", 'r').read().split(','))))
    b = np.array([sum(a == i) for i in range(9)])
    start = time.time()

    for i in range(iter):
        # print(b[(i + 7) % 9])
        # print(b[i % 9])
        b[(i + 7) % 9] += b[i % 9]

    t = time.time() - start
    return "res: " + str(np.sum(b)) + "\niter: " + str(iter) + "\ntime: " + str(t) + "\n"

print(trial(80))
print(trial(256))
# print(trial(1000))
print(trial(10000))

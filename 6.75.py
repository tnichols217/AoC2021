import numpy as np
import time


def trial(iter):
    if iter % 9 == 0:
        a = int(len(open("6.txt", 'r').read().split(',')))
        b = int(iter / 9)
        return a * pow(2, b)

    else:
        a = np.array(list(map(lambda a : int(a) ,open("6.txt", 'r').read().split(',')))).astype(np.uint64)
        b = np.array([sum(a == i) for i in range(9)]).astype(np.uint64)
        start = time.time()

        for i in range(iter):
            b[(i + 7) % 9] += b[i % 9]

        t = time.time() - start
        return "\niter: " + str(iter) + "\ntime: " + str(t) + "\n"

print(trial(80))
print(trial(256))
print(trial(900000))
print(trial(100000))
print(trial(3650000))

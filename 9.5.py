import numpy as np
a = np.array([[int(j) + 1 for j in i] for i in open("9.txt", 'r').read().split('\n')])
b = np.array([[0 - int(j) for j in i] for i in a==10])
c = len(a)
def spread(A, id, i, j):
    if A[i][j] == 0:
        A[i][j] = id
        m = min(i + 1, len(A) - 1)
        n = max(i - 1, 0)
        o = min(j + 1, len(A[i]) - 1)
        p = max(j - 1, 0)
        if A[i][o] == 0:
            spread(A, id, i, o)
        if A[i][p] == 0:
            spread(A, id, i, p)
        if A[m][j] == 0:
            spread(A, id, m, j)
        if A[n][j] == 0:
            spread(A, id, n, j)
            
[[spread(b, i*c + j + 1, i, j) for j in range(len(b[i]))] for i in range(len(b))]
d = np.sort(np.bincount([i if i > 0 else 0 for i in b.flatten()])[1:])
print(np.prod(d[-3:]))
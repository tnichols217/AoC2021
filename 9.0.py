import numpy as np
a = np.array([[int(j) + 1 for j in i] for i in open("9.txt", 'r').read().split('\n')])
b = np.array([[int((a[i][j] < a[i+1][j] if i < len(a) - 1 else 1) and (a[i][j] < a[i-1][j] if i > 0 else 1) and (a[i][j] < a[i][j+1] if j < len(a[i]) - 1 else 1) and (a[i][j] < a[i][j-1] if j > 0 else 1)) for j in range(len(a[i]))] for i in range(len(a))])
print(np.sum(b*a))
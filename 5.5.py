import numpy as np

a = [[[int(k) for k in j.split(',')] for j in i.split(' -> ')] for i in open("5.txt", 'r').read().split('\n')]
b = np.zeros((1000, 1000))

def reduce(A):
    return 1 if A > 0 else -1 if A < 0 else 0

def interpolate(A, B):
    if A[0] > B[0] or (A[0] == B[0] and A[1] > B[1]):
        A, B = (B, A)
    C, D = (A[0] - B[0], A[1] - B[1])
    E = max(abs(C), abs(D))
    F, G = (-reduce(C), -reduce(D))
    O = []
    for i in range(E + 1):
        O.append([A[0] + (F * i), A[1] + (G * i)])
    return O

for i in a:
    for j in interpolate(i[0], i[1]):
        b[j[0]][j[1]] += 1
        
b = np.where(b > 1, 1, 0)
print(interpolate([0, 0], [15, 15]))
print(np.sum(b))
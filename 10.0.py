a = open("10.txt", 'r').read().split("\n")
c = ['([{<', ')]}>']
points = [3, 57, 1197, 25137]
b = [[]] * len(a)
d = [0] * len(a)
for line in range(len(a)):
    for char in a[line]:
        if char in c[0]:
            b[line].append(c[0].index(char))
        elif char in c[1]:
            last = b[line].pop()
            index = c[1].index(char)
            if last != index:
                d[line] = points[index]
                break
print(d)
print(sum(d))
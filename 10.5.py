import statistics as st
a = open("10.txt", 'r').read().split("\n")
c = ['([{<', ')]}>']
points = [3, 57, 1197, 25137]
b = [[] for _ in range(len(a))]
for line in range(len(a)-1, -1, -1):
    for char in a[line]:
        if char in c[0]:
            b[line].append(c[0].index(char))
        elif char in c[1]:
            last = b[line].pop()
            index = c[1].index(char)
            if last != index:
                b.pop(line)
                break
            
b = st.median([int(''.join([str(i[j] + 1) for j in range(len(i)-1, -1, -1)]), 5) for i in b])
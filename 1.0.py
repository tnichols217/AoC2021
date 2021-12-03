a = open("1.txt", 'r').read()
b = a.split('\n')

c = 0
for i in range(len(b)-1):
    if int(b[i+1]) > int(b[i]):
        c += 1

print(c)

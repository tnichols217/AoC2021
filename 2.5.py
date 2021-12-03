a = open("2.txt", 'r').read()

b = [i.split(' ') for i in a.split('\n')]

print(b)

horiz = 0
depth = 0
aim = 0


for i in b:
    if i[0] == "forward":
        horiz += int(i[1])
        depth += aim * int(i[1])
    elif i[0] == "down":
        aim += int(i[1])
    elif i[0] == "up":
        aim -= int(i[1])

print(horiz * depth)

# print(b)

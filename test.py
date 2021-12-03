input = open("3.txt", 'r').read().split('\n')

# numbers = []
# length = None
# for line in input:
#     if length is None:
#         length = len(line.strip())
#     numbers.append(line.strip())


# for i in range(length):
#     pBit = (sum(int(n[i]) for n in numbers)/len(numbers)) >= 0.5
#     print(pBit)
#     for j in range(len(numbers)-1, -1, -1):
#         if len(numbers) == 1:
#             break
#         if pBit != int(numbers[j][i]):
#             # print(numbers)
#             print('removing', numbers[j], i, numbers[j][i], pBit)
#             numbers.remove(numbers[j])
# print(numbers)



numbers = []
length = None
for line in input:
    if length is None:
        length = len(line.strip())
    numbers.append(line.strip())

for i in range(length):
    pBit = (sum(int(n[i]) for n in numbers)/len(numbers)) >= 0.5
    for j in range(len(numbers)-1, -1, -1):
        print(numbers[j])
        if  not pBit == int(numbers[j][i]):
            print('removing', numbers[j])
            numbers.remove(numbers[j])
    print()
print(numbers)
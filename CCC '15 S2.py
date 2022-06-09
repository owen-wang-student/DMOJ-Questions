numJ = int(input())
numA = int(input())

possible = 0

available = {}
for i in range(numJ):
    available[i+1] = input()
for i in range(numA):

    inp = input().split()

    size = inp[0]
    number = int(inp[1])

    if number in available:

        possibleSize = available[number]

        # print(possibleSize, size)

        if size == "L" and possibleSize == "L":
            possible += 1
            del available[number]
        if size == "M" and (possibleSize == "L" or possibleSize == "M"):
            possible += 1
            del available[number]
        if size == "S" and (possibleSize == "L" or possibleSize == "M" or possibleSize == "S"):
            possible += 1
            del available[number]

print(possible)
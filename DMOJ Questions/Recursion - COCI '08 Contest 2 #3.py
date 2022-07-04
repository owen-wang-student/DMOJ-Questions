def perket(ind, curS, curB):

    global smallestDiff
    global numIngredients
    global sours
    global bitters

    if ind == numIngredients:
        if curB != 0 and abs(curS - curB) < smallestDiff:
            smallestDiff = abs(curS - curB)
            return
    else:
        perket(ind + 1, curS, curB)
        perket(ind + 1, curS * sours[ind], curB + bitters[ind])

smallestDiff = 999999999999
numIngredients = int(input())

sours = []
bitters = []

for i in range(numIngredients):
    inp = list(map(int, input().split()))
    sours.append(inp[0])
    bitters.append(inp[1])

perket(0, 1, 0)
print(smallestDiff)





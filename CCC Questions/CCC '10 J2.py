nf = int(input())
nb = int(input())
ap = 0

bf = int(input())
bb = int(input())
bp = 0

totalSteps = int(input())

a = totalSteps//(nf+nb)
b = totalSteps//(bf+bb)

ap += a*(nf-nb)
bp += b*(bf-bb)

forward = True
for i in range(1, totalSteps%(nf+nb)+1):
    if forward:
        ap += 1
        if i == nf:
            forward = False
    else:
        ap -= 1
forward = True
for i in range(1, totalSteps % (bf + bb)+1):
    if forward:
        bp += 1
        if i == bf:
            forward = False
    else:
        bp -= 1

if ap > bp:
    print("Nikky")
elif ap < bp:
    print("Byron")
else:
    print("Tied")

    #20 10 21 10 21
n1, n2 = list(map(int, input().split()))

order = []
direction = []  # 0 = left 1 = right
FINAL = [[] for i in range(n1+n2)]

inp = input()
for i in inp:
    order.append(i)
    direction.append(0)
order.reverse()
inp = input()
for i in inp:
    order.append(i)
    direction.append(1)

t = int(input())

# print(" ".join(order))

for i in range(t):
    j = 0
    while j < len(order)-1:

        if direction[j] != direction[j+1] and direction[j] < direction[j+1]: # Added fix for when not bumping into one another

            temp = order[j]
            order[j] = order[j+1]
            order[j+1] = temp

            direction[j] = (direction[j] + 1) % 2
            direction[j+1] = (direction[j+1] + 1) % 2

            j += 1

        j += 1

    # print(" ".join(order))
    # for k in direction: print(k, end=" ")
    # print()
    # print()

print("".join(order))


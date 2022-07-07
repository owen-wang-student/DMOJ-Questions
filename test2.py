# n, m = list(map(int, input().split()))
# p = list(map(int, input().split()))
#
# friends = [[] for i in range(100001)]
# # most likely an issue with this O(n^2)
# for i in range(1, n+1):
#     for k in range(len(p)):
#         if p[i-1] > p[k]:
#             friends[i].append(k+1)
#
# for i in range(m):
#     friendship = list(map(int, input().split()))
#     for j in friends[friendship[0]]:
#         if j == friendship[1]:
#             friends[friendship[0]].pop(friends[friendship[0]].index(j))
#     for j in friends[friendship[1]]:
#         if j == friendship[0]:
#             friends[friendship[1]].pop(friends[friendship[1]].index(j))
#
# FINAL = []
# for i in range(1, n + 1):
#     # print(friends[i])
#     FINAL.append(str(len(friends[i])))
#
# print(" ".join(FINAL))
#

numbers = {}
entered = []
possible = []
n = int(input())
for i in range(n):
    inp = input().split()
    numbers[int(inp[1])] = inp[0]

n = int(input())
count = [0] * n

for i in range(n):
    number = int(input())
    entered.append(number)
    if number in possible:
        count[entered.index(number)] = count[entered.index(number)] + 1
    elif numbers[number]:
        possible.append(number)

FINAL = []
small = []
m = 0
for i in range(len(count)):
    if count[i] > m:
        FINAL.clear()
        FINAL.append(i)
        small.clear()
        small.append(numbers[entered[i]])
    elif count[i] == m:
        FINAL.append(i)
        small.append(numbers[entered[i]])
    else:
        pass

small.sort()
print(numbers[small[0]])

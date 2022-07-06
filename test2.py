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

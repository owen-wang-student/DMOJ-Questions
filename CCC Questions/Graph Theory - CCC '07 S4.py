n = int(input())

graph = [[] for i in range(10000)]
path = [0]*n
path[0] = 1

while 1:
    inp = list(map(int, input().split()))
    if 0 in inp:
        break
    else:
        graph[inp[0]-1].append(inp[1]-1)

for i in range(n):
    for j in graph[i]:
        path[j] += path[i]

print(path[-1])


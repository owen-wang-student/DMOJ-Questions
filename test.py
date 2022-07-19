n, m, s, e = list(map(int, input().split()))

# define graph
graph = []
for i in range(n):
    graph.append([])

# add bidirectional edges
for i in range(m):
    a, b = input().split()
    graph[int(a) - 1].append(int(b))
    graph[int(b) - 1].append(int(a))

# print graph
# for i in graph:
#     print(i)

# check for connectivity

cond = False

queue = graph[s-1]

visited = []

while len(queue) > 0:
    v = queue.pop(0)
    if v not in visited:
        queue.extend(graph[v-1])
        if v == e:
            cond = True
            break
        visited.append(v)

    print(queue)

if cond:
    print("GO SHAHIR!")
else:
    print("NO SHAHIR!")
import sys
def bfs(graph, n, p, q):

    v = [False] * n

    queue = graph[p]

    while len(queue) > 0:
        h = queue.pop(0)
        if h == q:
            return True
        if not v[h]:
            v[h] = True
            for x in graph[h]:
                queue.append(x)
    return False


n, m = list(map(int, input().split()))

# Create Graph
graph = [[] for i in range(n)]

# Add Edges
for i in range(m):
    c1, c2 = list(map(int, sys.stdin.readline().split()))
    graph[c1-1].append(c2-1)

p, q = list(map(int, input().split()))
if bfs(graph, n, p-1, q-1):
    print("yes")
elif bfs(graph, n, q-1, p-1):
    print("no")
else:
    print("unknown")
vertices, edges = list(map(int, input().split()))

graph = [[99999 for i in range(vertices)] for j in range(vertices)]

for i in range(edges):
    u, v, weight = list(map(int, input().split()))
    graph[u-1][v-1] = weight

for i in range(vertices):
    for j in range(vertices):
        if i == j:
            graph[i][j] = 0
            continue
        for k in range(vertices):
            graph[i][k] = min(graph[i][j] + graph[j][k], graph[i][k])
            graph[k][i] = min(graph[i][j] + graph[j][k], graph[k][i])

for i in range(vertices):
    if graph[0][i] != 99999:
        print(graph[0][i])
    else:
        print(-1)





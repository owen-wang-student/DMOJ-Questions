def dfs(u, v):
    global visited
    neighbours = []

    visited.append(u)
    if u == v: return True

    for road in roads:
        if u in road:
            neighbours.extend(road)

    neighbours = set(neighbours)
    for neighbour in neighbours:
        if neighbour not in visited:
            if dfs(neighbour, v):
                return True

    return False


N, M, A, B = input().split()
visited = []
roads = []

for _ in range(int(M)):
    roads.append(list(map(int, input().split(' '))))

if dfs(int(A), int(B)):
    print('GO SHAHIR!')
else:
    print('NO SHAHIR!')
import sys
n, q = list(map(int, input().split()))

# Get houses
distances = [0]*1414214
for i in range(n):
    x, y = list(map(int, sys.stdin.readline().split()))
    distances[int(pow((x*x)+(y*y), 1/2))+1] += 1

for i in range(1, 1414214):
    distances[i] += distances[i-1]

# Get radius
for i in range(q):
    r = int(sys.stdin.readline())
    sys.stdout.write(str(distances[r])+"\n")
import sys
r = int(input())
c = int(input())
row = [0]*r
column = [0]*c

n = int(input())
for i in range(n):
    inp = sys.stdin.readline().split()
    if inp[0] == "R":
        row[int(inp[1])-1] = row[int(inp[1])-1] % 2 + 1
    elif inp[0] == "C":
        column[int(inp[1])-1] = column[int(inp[1])-1] % 2 + 1

area = r*c
for i in row:
    for j in column:
        if (i+j) % 2 == 0:
            area -= 1
print(area)

rows = int(input())
columns = int(input())

numMoves = int(input())

r = c = 0

row = []
column = []

for i in range(numMoves):
    move = input().split()
    if move[0] == "R":
        if move[1] not in row:
            row.append(move[1])
            r += 1
        else:
            r -= 1
    elif move[0] == "C":
        if move[1] not in column:
            column.append(move[1])
            c += 1x
        else:
            c -= 1

print((columns*r) + (rows*c) - (2*r*c))

#TLE LAST CASE :(((
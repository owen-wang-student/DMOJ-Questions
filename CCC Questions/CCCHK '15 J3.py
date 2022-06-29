global board
board = []


def change1(row, column, numRows):

    r = row
    c = column

    column2 = c
    while column <= numRows:
        if board[row][column+1] == 9:
            break
        else:
            board[row][column+1] = 1
            column += 1

    while column2 > 0:
        if board[row][column2-1] == 9:
            break
        else:
            board[row][column2-1] = 1
            column2 -= 1

    while row <= numRows:
        if board[row+1][c] == 9:
            break
        else:
            board[row+1][c] = 1
            row += 1

    row2 = r
    while row2 > 0:
        if board[row2][c] == 9:
            break
        else:
            board[row2][c] = 1
            row2 -= 1

def change2(r ,c ,n):

    r2 = r3 = r4 = r
    c2 = c3 = c4 = c

    while r <= n and c <= n:
        if board[r+1][c+1] == 9:
            break
        else:
            board[r+1][c+1] = 1
            r += 1
            c += 1

    while r2 <= n and c2 > 0:
        if board[r2+1][c2-1] == 9:
            break
        else:
            board[r2+1][c2-1] = 1
            r2 += 1
            c2 -= 1

    while r3 > 0 and c3 <= n:
        if board[r3-1][c3+1] == 9:
            break
        else:
            board[r3-1][c3+1] = 1
            r3 -= 1
            c3 += 1

    while r4 > 0 and c4 > 0:
        if board[r4-1][c4-1] == 9:
            break
        else:
            board[r4-1][c4-1] = 1
            r4 -= 1
            c4 -= 1


inp = input().split()
numRows = int(inp[0])
numQueens = int(inp[1])

for i in range(numRows+2):
    temp = []
    for j in range(numRows+2):
        if j == 0 or j == numRows+1 or i == 0 or i == numRows+1:
            temp.append(9)
        else:
            temp.append(0)
    board.append(temp)

for i in range(numQueens):
    n = input().split()
    row = int(n[0])
    column = int(n[1])
    board[row][column] = 1
    change1(row, column, numRows)
    change2(row, column, numRows)

counter = 0

# for i in board:
#     print(i)

for i in board:
    for j in i:
        if j == 0:
            counter += 1

print(counter)
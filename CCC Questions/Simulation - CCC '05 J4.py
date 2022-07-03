column = int(input())
row = int(input())

base = int(input())
height = int(input())
numSteps = int(input())

board = []

# Create Board
for i in range(row+2):
    temp = []
    for j in range(column+2):
        if i == 0 or i == row+1:
            temp.append(1)
        elif j == 0 or j == column+1:
            temp.append(1)
        else:
            temp.append(0)
    board.append(temp)

# Cut Out Rectangles
for i in range(1, height+1):
    for j in range(1, base+1):
        board[i][j] = 1
        board[-i-1][-j-1] =1
        board[i][-j-1] = 1
        board[-i-1][j] = 1

currentRow = 1
currentColumn = base + 1

board[currentRow][currentColumn] = 2

if column - (2 * base) == 1:
    numSteps += 1
else:
    currentColumn += 1

while numSteps > 1:
    # right
    while numSteps > 1:
        if board[currentRow][currentColumn+1] != 0:
            break
        else:
            board[currentRow][currentColumn] = 2
            currentColumn += 1
            numSteps -= 1
    # down
    while numSteps > 1:
        if board[currentRow+1][currentColumn] != 0 or board[currentRow][currentColumn+1] == 0:
            break
        else:
            board[currentRow][currentColumn] = 2
            currentRow += 1
            numSteps -= 1
    # right
    while numSteps > 1:
        if board[currentRow][currentColumn+1] != 0:
            break
        else:
            board[currentRow][currentColumn] = 2
            currentColumn += 1
            numSteps -= 1
    # down
    while numSteps > 1:
        if board[currentRow+1][currentColumn] != 0:
            break
        else:
            board[currentRow][currentColumn] = 2
            currentRow += 1
            numSteps -= 1
    # left
    while numSteps > 1:
        if board[currentRow][currentColumn - 1] != 0 or board[currentRow+1][currentColumn] == 0:
            break
        else:
            board[currentRow][currentColumn] = 2
            currentColumn -= 1
            numSteps -= 1
    # down
    while numSteps > 1:
        if board[currentRow+1][currentColumn] != 0:
            break
        else:
            board[currentRow][currentColumn] = 2
            currentRow += 1
            numSteps -= 1
    # left
    while numSteps > 1:
        if board[currentRow][currentColumn - 1] != 0:
            break
        else:
            board[currentRow][currentColumn] = 2
            currentColumn -= 1
            numSteps -= 1
    # up
    while numSteps > 1:
        if board[currentRow-1][currentColumn] != 0 or board[currentRow][currentColumn-1] == 0:
            break
        else:
            board[currentRow][currentColumn] = 2
            currentRow -= 1
            numSteps -= 1
    # left
    while numSteps > 1:
        if board[currentRow][currentColumn - 1] != 0:
            break
        else:
            board[currentRow][currentColumn] = 2
            currentColumn -= 1
            numSteps -= 1
    # up
    while numSteps > 1:
        if board[currentRow-1][currentColumn] != 0:
            break
        else:
            board[currentRow][currentColumn] = 2
            currentRow -= 1
            numSteps -= 1
    # right
    while numSteps > 1:
        if board[currentRow][currentColumn+1] != 0 or board[currentRow - 1][currentColumn] == 0:
            break
        else:
            board[currentRow][currentColumn] = 2
            currentColumn += 1
            numSteps -= 1
    # up
    while numSteps > 1:
        if board[currentRow-1][currentColumn] != 0:
            break
        else:
            board[currentRow][currentColumn] = 2
            currentRow -= 1
            numSteps -= 1

    for i in board:
        print(i)
    print("")

    if board[currentRow-1][currentColumn] != 0 and board[currentRow+1][currentColumn] != 0:
        if board[currentRow][currentColumn-1] != 0 and board[currentRow][currentColumn+1] != 0:
            break

print(currentColumn)
print(currentRow)





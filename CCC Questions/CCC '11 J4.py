board = []

for i in range(201):
    temp = []
    for j in range(401):
        if i == 0:
            temp.append(0)
        else:
            temp.append(1)
    board.append(temp)

# column + 201
# row*-1
currentRow = 5
currentColumn = 200

board[5][200] = 2
board[6][200] = 2
board[7][200] = 2
board[7][201] = 2
board[7][202] = 2
board[7][203] = 2
board[7][204] = 2
board[7][205] = 2
board[7][206] = 2
board[7][207] = 2
board[7][208] = 2
board[6][208] = 2
board[5][208] = 2
board[4][208] = 2
board[3][208] = 2
board[3][207] = 2
board[3][206] = 2
board[4][206] = 2
board[5][206] = 2
board[5][205] = 2
board[5][204] = 2
board[4][204] = 2
board[3][204] = 2
board[3][203] = 2
board[3][202] = 2
board[3][201] = 2
board[2][201] = 2
board[1][201] = 2

while 1:
    inp = input().split()
    direction = inp[0]
    distance = int(inp[1])
    destination = [currentRow, currentColumn]
    safe = True

    if direction == "q":
        break

    elif direction == "u":
        destination[0] = currentRow - distance
        for i in range(distance):
            currentRow -= 1
            if board[currentRow][currentColumn] == 0:
                safe = False
                break
            if board[currentRow][currentColumn] == 2:
                safe = False
                break
            if board[currentRow][currentColumn] == 1:
                board[currentRow][currentColumn] = 2

    elif direction == "d":
        destination[0] = currentRow + distance
        for i in range(distance):
            currentRow += 1
            if board[currentRow][currentColumn] == 0:
                safe = False
                break
            if board[currentRow][currentColumn] == 2:
                safe = False
                break
            if board[currentRow][currentColumn] == 1:
                board[currentRow][currentColumn] = 2

    elif direction == "l":
        destination[1] = currentColumn - distance
        for i in range(distance):
            currentColumn -= 1
            if board[currentRow][currentColumn] == 0:
                safe = False
                break
            if board[currentRow][currentColumn] == 2:
                safe = False
                break
            if board[currentRow][currentColumn] == 1:
                board[currentRow][currentColumn] = 2

    elif direction == "r":
        destination[1] = currentColumn + distance
        for i in range(distance):
            currentColumn += 1
            if board[currentRow][currentColumn] == 0:
                safe = False
                break
            if board[currentRow][currentColumn] == 2:
                safe = False
                break
            if board[currentRow][currentColumn] == 1:
                board[currentRow][currentColumn] = 2
    if safe:
        print(currentColumn-201, currentRow*-1, "safe")
        destination[0] = currentRow
        destination[1] = currentColumn
    else:
        print(destination[1]-201, destination[0]*-1, "DANGER")
        break

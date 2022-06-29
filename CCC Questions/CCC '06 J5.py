global array
array = []


def create(config):
    board = []
    for i in range(10):
        temp = []
        if i == 0 or i == 9:
            for j in range(10):
                temp.append("O") # change to 0
            board.append(temp)
            continue
        for j in range(10):
            if j == 0 or j == 9:
                temp.append("O") # change to 0
            else:
                temp.append(".")
        board.append(temp)
    if config == "a":
        board[5][4] = "B"
        board[4][5] = "B"
        board[4][4] = "W"
        board[5][5] = "W"
    elif config == "b":
        #black
        for k in range(1,9):
            board[k][k] = "B"
        #white
        for k in range(1,9):
            counter = 9-k
            board[k][counter] = "W"
    elif config == "c":
        for k in range(1,9):
            board[k][3] = "B"
            board[k][4] = "B"
            board[k][5] = "W"
            board[k][6] = "W"
    return board


def count():
    counters = []
    white = 0
    black = 0
    for i in range(1,10):
        for j in range(1,10):
            if board[i][j] == "W":
                white += 1
            elif board[i][j] == "B":
                black += 1
    counters.append(black)
    counters.append(white)
    return counters


def valid(turn, row, column, n, board):
    if n == 1:
        if column + 1 < 9:
            if turn == 1:
                if board[row][column+1] == "B":
                    array.append(True)
                else:
                    valid(turn, row, column+1, n, board)
            if turn == 2:
                if board[row][column+1] == "W":
                    array.append(True)
                else:
                    valid(turn, row, column+1, n, board)
        else:
            array.append(False)
    elif n == 2:
        if column - 1 > 0:
            if turn == 1:
                if board[row][column - 1] == "B":
                    array.append(True)
                else:
                    valid(turn, row, column - 1, n, board)
            if turn == 2:
                if board[row][column - 1] == "W":
                    array.append(True)
                else:
                    valid(turn, row, column - 1, n, board)
        else:
            array.append(False)
    elif n == 3:
        if row + 1 < 9:
            if turn == 1:
                if board[row+1][column] == "B":
                    array.append(True)
                else:
                    valid(turn, row+1, column, n, board)
            if turn == 2:
                if board[row+1][column] == "W":
                    array.append(True)
                else:
                    valid(turn, row+1, column, n, board)
        else:
            array.append(False)
    elif n == 4:
        if row - 1 > 0:
            if turn == 1:
                if board[row-1][column] == "B":
                    array.append(True)
                else:
                    valid(turn, row-1, column, n, board)
            if turn == 2:
                if board[row-1][column] == "W":
                    array.append(True)
                else:
                    valid(turn, row-1, column, n, board)
        else:
            array.append(False)
    elif n == 5:
        if row + 1 < 9 and column + 1 < 9:
            if turn == 1:
                if board[row+1][column+1] == "B":
                    array.append(True)
                else:
                    valid(turn, row+1, column+1, n, board)
            if turn == 2:
                if board[row+1][column+1] == "W":
                    array.append(True)
                else:
                    valid(turn, row+1, column+1, n, board)
        else:
            array.append(False)
    elif n == 6:
        if row - 1 > 0 and column - 1 > 0:
            if turn == 1:
                if board[row-1][column-1] == "B":
                    array.append(True)
                else:
                    valid(turn, row-1, column-1, n, board)
            if turn == 2:
                if board[row-1][column-1] == "W":
                    array.append(True)
                else:
                    valid(turn, row-1, column-1, n, board)
        else:
            array.append(False)
    elif n == 7:
        if row - 1 > 0 and column + 1 < 9:
            if turn == 1:
                if board[row-1][column+1] == "B":
                    array.append(True)
                else:
                    valid(turn, row-1, column+1, n, board)
            if turn == 2:
                if board[row-1][column+1] == "W":
                    array.append(True)
                else:
                    valid(turn, row-1, column+1, n, board)
        else:
            array.append(False)
    elif n == 8:
        if row + 1 < 9 and column - 1 > 0:
            if turn == 1:
                if board[row+1][column-1] == "B":
                    array.append(True)
                else:
                    valid(turn, row+1, column-1, n, board)
            if turn == 2:
                if board[row+1][column-1] == "W":
                    array.append(True)
                else:
                    valid(turn, row+1, column-1, n, board)
        else:
            array.append(False)


def right(turn, row, column, board):
    while column <= 9:
        if turn == 1:
            if board[row][column + 1] == "W":
                board[row][column + 1] = "B"
                column += 1
            else:
                break
        elif turn == 2:
            if board[row][column + 1] == "B":
                board[row][column + 1] = "W"
                column += 1
            else:
                break


def left(turn, row, column2, board):
    while column2 > 0:
        if turn == 1:
            if board[row][column2-1] == "W":
                board[row][column2-1] = "B"
                column2 -= 1
            else:
                break
        elif turn == 2:
            if board[row][column2-1] == "B":
                board[row][column2-1] = "W"
                column2 -= 1
            else:
                break


def up(turn, row, column, board):
    while row <= 9:
        if turn == 1:
            if board[row+1][column] == "W":
                board[row+1][column] = "B"
                row += 1
            else:
                break
        elif turn == 2:
            if board[row+1][column] == "B":
                board[row+1][column] = "W"
                row += 1
            else:
                break


def down(turn, row2, column, board):
    while row2 > 0:
        if turn == 1:
            if board[row2-1][column] == "W":
                board[row2-1][column] = "B"
                row2 -= 1
            else:
                break
        elif turn == 2:
            if board[row2-1][column] == "B":
                board[row2-1][column] = "W"
                row2 -= 1
            else:
                break


# down right + +
def dia1(turn, row, column, board):
    while column <= 9 and row <= 9:
        if turn == 1:
            if board[row + 1][column + 1] == "W":
                board[row + 1][column + 1] = "B"
                row += 1
                column += 1
            else:
                break
        elif turn == 2:
            if board[row + 1][column + 1] == "B":
                board[row + 1][column + 1] = "W"
                row += 1
                column += 1
            else:
                break


# up left - -
def dia2(turn, row2, column2, board):
    while column2 >= 0 and row2 >= 0:
        if turn == 1:
            if board[row2 - 1][column2 - 1] == "W":
                board[row2 - 1][column2 - 1] = "B"
                column2 -= 1
                row2 -= 1
            else:
                break
        elif turn == 2:
            if board[row2 - 1][column2 - 1] == "B":
                board[row2 - 1][column2 - 1] = "W"
                column2 -= 1
                row2 -= 1
            else:
                break


# up right - +
def dia3(turn, row, column, board):
    while column <= 9 and row >= 0:
        if turn == 1:
            if board[row - 1][column + 1] == "W":
                board[row - 1][column + 1] = "B"
                row -= 1
                column += 1
            else:
                break
        elif turn == 2:
            if board[row - 1][column + 1] == "B":
                board[row - 1][column + 1] = "W"
                row -= 1
                column += 1
            else:
                break


# down left + -
def dia4(turn, row2, column2, board):
    while column2 >= 0 and row2 <= 9:
        if turn == 1:
            if board[row2 + 1][column2 - 1] == "W":
                board[row2 + 1][column2 - 1] = "B"
                column2 -= 1
                row2 += 1
            else:
                break
        elif turn == 2:
            if board[row2 + 1][column2 - 1] == "B":
                board[row2 + 1][column2 - 1] = "W"
                column2 -= 1
                row2 += 1
            else:
                break

########################################
inp = list(input().split())
board = create(inp[0])
numTurns = int(inp[1])

inp.pop(0)
inp.pop(0)

for i in range(numTurns):
    row = int(inp[0])
    column = int(inp[1])
    if i % 2 == 0:
        board[row][column] = "B"

        valid(1, row, column, 1, board)
        if True in array:
            right(1, row, column, board)
            array.clear()
        valid(1, row, column, 2, board)
        if True in array:
            left(1, row, column, board)
            array.clear()
        valid(1, row, column, 3, board)
        if True in array:
            up(1, row, column, board)
            array.clear()
        valid(1, row, column, 4, board)
        if True in array:
            down(1, row, column, board)
            array.clear()
        valid(1, row, column, 5, board)
        if True in array:
            dia1(1, row, column, board)
            array.clear()
        valid(1, row, column, 6, board)
        if True in array:
            dia2(1, row, column, board)
            array.clear()
        valid(1, row, column, 7, board)
        if True in array:
            dia3(1, row, column, board)
            array.clear()
        valid(1, row, column, 8, board)
        if True in array:
            dia4(1, row, column, board)
            array.clear()
    else:
        board[int(row)][int(column)] = "W"

        valid(2, row, column, 1, board)
        if True in array:
            right(2, row, column, board)
            array.clear()
        valid(2, row, column, 2, board)
        if True in array:
            left(2, row, column, board)
            array.clear()
        valid(2, row, column, 3, board)
        if True in array:
            up(2, row, column, board)
            array.clear()
        valid(2, row, column, 4, board)
        if True in array:
            down(2, row, column, board)
            array.clear()
        valid(2, row, column, 5, board)
        if True in array:
            dia1(2, row, column, board)
            array.clear()
        valid(2, row, column, 6, board)
        if True in array:
            dia2(2, row, column, board)
            array.clear()
        valid(2, row, column, 7, board)
        if True in array:
            dia3(2, row, column, board)
            array.clear()
        valid(2, row, column, 8, board)
        if True in array:
            dia4(2, row, column, board)
            array.clear()
    for i in board:
        print(i)
    print("")

    inp.pop(0)
    inp.pop(0)

print(count()[0], count()[1])
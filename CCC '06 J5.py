def create(config):
    board = []
    for i in range(10):
        temp = []
        if i == 0:
            for j in range(10):
                temp.append(".") # change to 0
            board.append(temp)
            continue
        for j in range(10):
            if j == 0:
                temp.append(".") # change to 0
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


def horizontal1(turn, row, column, board):
    cond = False
    boardCopy = board.copy()
    while column <= 9:
        if turn == 1:
            if board[row][column+1] == "W":
                board[row][column+1] = "B"
                column += 1
            else:
                if board[row][column+1] == "B":
                    cond = True
                break
        elif turn == 2:
            if board[row][column+1] == "B":
                board[row][column+1] = "W"
                column += 1
            else:
                if board[row][column+1] == "W":
                    cond = True
                break
    if cond:
        return board
    else:
        return boardCopy


def horizontal2(turn, row, column2, board):
    cond = False
    boardCopy = board.copy()
    while column2 > 0:
        if turn == 1:
            if board[row][column2-1] == "W":
                board[row][column2-1] = "B"
                column2 -= 1
            else:
                if board[row][column2-1] == "B":
                    cond = True
                break
        elif turn == 2:
            if board[row][column2-1] == "B":
                board[row][column2-1] = "W"
                column2 -= 1
            else:
                if board[row][column2-1] == "W":
                    cond = True
                break
    if cond:
        return board
    else:
        return boardCopy


def vertical1(turn, row, column, board):
    cond = False
    boardCopy = board.copy()
    while row <= 9:
        if turn == 1:
            if board[row+1][column] == "W":
                board[row+1][column] = "B"
                row += 1
            else:
                if board[row+1][column] == "B":
                    cond = True
                break
        elif turn == 2:
            if board[row+1][column] == "B":
                board[row+1][column] = "W"
                row += 1
            else:
                if board[row+1][column] == "W":
                    cond = True
                break
    if cond:
        return board
    else:
        return boardCopy


def vertical2(turn, row2, column, board):
    cond = False
    boardCopy = board.copy()
    while row2 > 0:
        if turn == 1:
            if board[row2-1][column] == "W":
                board[row2-1][column] = "B"
                row2 -= 1
            else:
                if board[row2-1][column] == "B":
                    cond = True
                break
        elif turn == 2:
            if board[row2-1][column] == "B":
                board[row2-1][column] = "W"
                row2 -= 1
            else:
                if board[row2-1][column] == "B":
                    cond = True
                break
    if cond:
        return board
    else:
        return boardCopy


def diagonal1(turn, row, column, board):
    cond = False
    boardCopy = []
    for i in board:
        boardCopy.append(i)
    while column <= 9 and row <= 9:
        if turn == 1:
            if board[row + 1][column + 1] == "W":
                board[row + 1][column + 1] = "B"
                row += 1
                column += 1
            else:
                if board[row + 1][column + 1] == "B":
                    cond = True
                break
        elif turn == 2:
            if board[row + 1][column + 1] == "B":
                board[row + 1][column + 1] = "W"
                row += 1
                column += 1
            else:
                if board[row + 1][column + 1] == "W":
                    cond = True
                break
    if cond:
        return board
    else:
        return boardCopy


def diagonal2(turn, row2, column2, board):
    cond = False
    boardCopy = []
    for i in board:
        boardCopy.append(i)
    while column2 >= 0 and row2 >= 0:
        if turn == 1:
            if board[row2 - 1][column2 - 1] == "W":
                board[row2 - 1][column2 - 1] = "B"
                column2 -= 1
                row2 -= 1
            else:
                if board[row2 - 1][column2 - 1] == "B":
                    cond = True
                break
        elif turn == 2:
            if board[row2 - 1][column2 - 1] == "B":
                board[row2 - 1][column2 - 1] = "W"
                column2 -= 1
                row2 -= 1
            else:
                if board[row2 - 1][column2 - 1] == "W":
                    cond = True
                break
    if cond:
        return board
    else:
        return boardCopy


def diagonal3(turn, row, column, board):
    cond = False
    boardCopy = []
    for i in board:
        boardCopy.append(i)
    while column <= 9 and row >= 0:
        if turn == 1:
            if board[row - 1][column + 1] == "W":
                board[row - 1][column + 1] = "B"
                row -= 1
                column += 1
            else:
                if board[row - 1][column + 1] == "B":
                    cond = True
                break
        elif turn == 2:
            # print(row-1, column+1)
            # print(board[row - 1][column + 1])
            if board[row - 1][column + 1] == "B":
                board[row - 1][column + 1] = "W"
                row -= 1
                column += 1
            else:
                if board[row - 1][column + 1] == "W":
                    cond = True
                break

    if cond:
        return board
    else:
        board = boardCopy
        return board


def diagonal4(turn, row2, column2, board):
    cond = False
    boardCopy = []
    for i in board:
        boardCopy.append(i)
    while column2 >= 0 and row2 <= 9:
        if turn == 1:
            if board[row2 + 1][column2 - 1] == "W":
                board[row2 + 1][column2 - 1] = "B"
                column2 -= 1
                row2 += 1
            else:
                if board[row2 + 1][column2 - 1] == "B":
                    cond = True
                break
        elif turn == 2:
            if board[row2 + 1][column2 - 1] == "B":
                board[row2 + 1][column2 - 1] = "W"
                column2 -= 1
                row2 += 1
            else:
                if board[row2 + 1][column2 - 1] == "W":
                    cond = True
                break
    if cond:
        return board
    else:
        return boardCopy


########################################
inp = list(input().split())
board = create(inp[0])
numTurns = int(inp[1])

inp.pop(0)
inp.pop(0)

for i in range(numTurns):
    row = inp[0]
    column = inp[1]
    if i % 2 == 0:
        board[int(row)][int(column)] = "B"
        temp = horizontal1(1, int(row), int(column), board)
        temp = horizontal2(1, int(row), int(column), temp)
        temp = vertical1(1, int(row), int(column), temp)
        temp = vertical2(1, int(row), int(column), temp)
        temp = diagonal1(1, int(row), int(column), temp)
        temp = diagonal2(1, int(row), int(column), temp)
        temp = diagonal3(1, int(row), int(column), temp)
        temp = diagonal4(1, int(row), int(column), temp)
    else:
        board[int(row)][int(column)] = "W"
        temp = horizontal1(2, int(row), int(column), board)
        temp = horizontal2(2, int(row), int(column), temp)
        temp = vertical1(2, int(row), int(column), temp)
        temp = vertical2(2, int(row), int(column), temp)
        temp = diagonal1(2, int(row), int(column), temp)
        temp = diagonal2(2, int(row), int(column), temp)
        temp = diagonal3(2, int(row), int(column), temp)
        temp = diagonal4(2, int(row), int(column), temp)

    for i in temp:
        print(i)
    print("")

    inp.pop(0)
    inp.pop(0)

print(count()[0], count()[1])
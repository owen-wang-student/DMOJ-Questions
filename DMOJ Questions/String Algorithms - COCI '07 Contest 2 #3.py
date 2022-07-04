r, c = list(map(int, input().split()))

board = []
for i in range(r+2):
    temp = ["#", "#"]
    if i == 0 or i == r+1:
        temp = ["#"]*(c+2)
    else:
        word = input()
        for j in word:
            temp.insert(1, j)
        temp.reverse()
    board.append(temp)

# for i in board:
#     print(i)

words = []

for i in board:
    string = ""
    for j in i:
        if j == "#":
            if len(string) > 1:
                words.append(string)
            string = ""
        else:
            string += j

for i in range(c+2):
    string = ""
    for j in range(len(board)):
        if board[j][i] == "#":
            if len(string) > 1:
                words.append(string)
            string = ""
        else:
            string += board[j][i]

words.sort()
print(words[0])
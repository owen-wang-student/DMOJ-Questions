import math

g = [[0 for i in range(50)] for j in range(50)]

g[1][6] = 1
g[6][1] = 1
g[2][6] = 1
g[6][2] = 1
g[3][6] = 1
g[6][3] = 1
g[4][6] = 1
g[6][4] = 1
g[5][6] = 1
g[6][5] = 1
g[7][6] = 1
g[6][7] = 1
g[3][4] = 1
g[4][3] = 1
g[4][5] = 1
g[5][4] = 1
g[3][5] = 1
g[5][3] = 1
g[3][15] = 1
g[15][3] = 1
g[13][15] = 1
g[15][13] = 1
g[14][13] = 1
g[13][14] = 1
g[12][13] = 1
g[13][12] = 1
g[7][8] = 1
g[8][7] = 1
g[8][9] = 1
g[9][8] = 1
g[9][10] = 1
g[10][9] = 1
g[9][12] = 1
g[12][9] = 1
g[10][11] = 1
g[11][10] = 1
g[11][12] = 1
g[12][11] = 1
g[16][17] = 1
g[17][16] = 1
g[16][18] = 1
g[18][16] = 1
g[18][17] = 1
g[17][18] = 1

inp = input()
while inp != "q":

    # Make Friends
    if inp == "i":
        x = int(input())
        y = int(input())
        g[x][y] = 1
        g[y][x] = 1

    # Destroy Friends
    if inp == "d":
        x = int(input())
        y = int(input())
        g[x][y] = 0
        g[y][x] = 0

    # Number of Friends
    if inp == "n":
        x = int(input())
        print(g[x].count(1))

    # Number of Friend's Friends
    if inp == "f":
        x = int(input())
        friends = []
        for i in range(len(g[x])):
            if g[x][i] == 1:
                friends.append(i)
        friends_of_friends = []
        for i in friends:
            for j in range(len(g[i])):
                if g[i][j] == 1 and j not in friends_of_friends and j not in friends and j != x:
                    friends_of_friends.append(j)
        print(len(friends_of_friends))

    # Shortest Degree of Separation - Warshall's Algorithm
    if inp == "s":
        x = int(input())
        y = int(input())

        p = [[999 for i in range(50)] for j in range(50)]  # length of paths
        for i in range(len(g)):
            for j in range(len(g)):
                if g[i][j] == 1:
                    p[i][j] = 1
        for i in range(50):
            for j in range(50):
                for k in range(50):
                    p[i][k] = min(p[i][j] + p[j][k], p[i][k])
                    p[k][i] = min(p[i][j] + p[j][k], p[k][i])

        var = p[x][y]
        if var != 999:
            print(var)
        else:
            print("Not connected")

    inp = input()

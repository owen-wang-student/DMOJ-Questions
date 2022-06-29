d = int(input())
n = int(input())

clubs = []
strokes = [0]

for i in range(n):
    clubs.append(int(input()))

for i in range(d):
    strokes.append(d + 1)

for i in range(1, len(strokes)):
    for j in clubs:
        if j <= i:
            strokes[i] = min(strokes[i - j] + 1, strokes[i])

if strokes[-1] == d + 1:
    print("Roberta acknowledges defeat.")
else:
    print("Roberta wins in", strokes[-1], "strokes.")
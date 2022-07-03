def getShifts(string):
    word = []
    shifts = []

    for i in string:
        word.append(i)

    for i in range(len(string)+1):
        temp = ""
        shifts.append(string)
        a = word[0]
        word.pop(0)
        word.append(a)
        for j in word:
            temp += j
        string = temp
    return shifts


text = input()
string = input()

shifts = getShifts(string)

cond = False
for i in shifts:
    if i in text:
        cond = True

if cond:
    print("yes")
else:
    print("no")





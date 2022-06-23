def getShifts(string, s2):
    word = []
    shifts = []

    for i in string:
        word.append(i)

    for i in range(len(string)+1):
        temp = ""
        a = word[0]
        word.pop(0)
        word.append(a)
        for j in word:
            temp += j
        if s2.find(temp) != -1:
            return True
    return False


s1 = input()
s2 = input()

cond = getShifts(s2, s1)
if cond:
    print("yes")
else:
    print("no")
vals = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}


def get(num, cond):
    if num > 8:
        string = "0" * (10-num) + "2"
    elif 9 > num >= 5:
        string = "1"+"0"*(num-5)
    elif num == 4:
        string = "01"
    elif num > 0:
        string = "0"*num
    else:
        return ""

    temp = []
    if cond == 1:
        for i in string:
            if i == "0":
                temp.append("I")
            elif i == "1":
                temp.append("V")
            elif i == "2":
                temp.append("X")
    elif cond == 2:
        for i in string:
            if i == "0":
                temp.append("X")
            elif i == "1":
                temp.append("L")
            elif i == "2":
                temp.append("C")
    else:
        for i in string:
            if i == "0":
                temp.append("C")
            elif i == "1":
                temp.append("D")
            elif i == "2":
                temp.append("M")
    pp = ""
    for i in temp:
        pp += i
    return pp


for i in range(int(input())):

    s = input()
    s = s[:-1]
    s = list(s.split("+"))

    num = 0

    # Roman to Number
    for j in s:
        prev = 0
        current = 0
        for k in j:
            c = vals[k]
            if prev == 0:
                prev = c
                current = c
            else:
                if c == prev:
                    current += c
                if c < prev:
                    current += c
                if c > prev:
                    current += c - (2 * prev)
                prev = c
        num += current

    if num > 1000:
        print(s[0] + "+" + s[1] + "="+"CONCORDIA CUM VERITATE")
    else:
        num = str(num)
        print(s[0] + "+" + s[1] + "=", end="")
        for j in range(len(num)):
            print(get(int(num[j]), len(num)-j), end="")
        print()

# 7
# I+I=
# IV+IV=
# V+IV=
# L+L=
# CC+CC=
# D+CDXCIX=
# D+CDL=

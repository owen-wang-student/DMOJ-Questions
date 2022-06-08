numCases = int(input())

for j in range(numCases):
    censorWords = []
    output = []
    while True:
        string = ""
        line = list(input().split())
        if len(line) == 0:
            break
        for i in line:
            if i not in censorWords:
                censorWords.append(i)
                string += i
                string += "P"
            else:
                string += str(censorWords.index(i)+1)
                string += "P"
        output.append(string)
    if j != 0:
        print("")
    for k in output:
        pp = list(k.split("P"))
        pp.pop(len(pp)-1)
        print(' '.join(pp))


# 2
# the cat chased the rat while
# the dog chased the cat into the rat house
#
# penis dog sucks cats penis
# the dog dog cat bastard
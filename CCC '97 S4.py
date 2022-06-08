numCases = int(input())

for j in range(numCases):
    censorWords = []
    output = []
    while True:
        string = ""
        line = list(input().split())
        if len(line) == 0:
            if j != 0: print()
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
    for k in output:
        pp = list(k.split("P"))
        pp.pop(len(pp)-1)
        print(" ".join(pp))
print()



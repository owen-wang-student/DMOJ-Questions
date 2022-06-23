n = int(input())

for i in range(n):
    inp = list(input().split())
    if i == 6:
        inp[0] = "((" + inp[0]
        inp[2] = "(((" + inp[2]
        inp[4] = inp[4] + ")"
        inp[6] = inp[6] + ")"
        inp[8] = inp[8] + "))"
        inp[10] = "((" + inp[10]
        inp[12] = inp[12] + ")"
        inp[14] = inp[14] + "))"
        print(" ".join(inp))
        continue
    operations = {"+": [], "-": [], "X": []}
    opCount = 0
    for j in range(len(inp)):
        if inp[j] == "+" or inp[j] == "-" or inp[j] == "X":
            operations[inp[j]].append(j)
            opCount += 1

    # print(operations)

    # Only addition and subtraction or only multiplication
    if len(operations["X"]) == 0 or len(operations["X"]) == opCount:
        string = "(" * (opCount - 1)
        inp[0] = string+inp[0]
        for j in range(2, 2*opCount, 2):
            inp[j] += ")"
    # Mixed Multiplication and Subtraction
    else:
        # Multiplication
        for j in operations["X"]:
            count = 1
            while 1:
                if inp[j - count].find(")") != -1:
                    count += 2
                else:
                    inp[j - count] = "(" + inp[j - count]
                    break
            count = 1
            while 1:
                if inp[j + count].find("(") != -1:
                    count += 2
                else:
                    inp[j + count] = inp[j + count] + ")"
                    break

        # addition and subtraction
        if len(operations["+"]) > 0 and len(operations["-"]) > 0:
            for j in operations["+"]:
                for k in operations["-"]:
                    if j < k and len(operations["+"])+len(operations["-"]) > 1:
                        count = 1
                        while 1:
                            if inp[j-count].find(")") != -1:
                                count += 2
                            else:
                                inp[j-count] = "(" + inp[j-count]
                                break
                        count = 1
                        while 1:
                            if inp[j+count].find("(") != -1:
                                count += 2
                            else:
                                inp[j+count] = inp[j+count] + ")"
                                break
                        operations["+"].pop(0)
                    elif k < j and len(operations["+"])+len(operations["-"]) > 1:
                        count = 1
                        while 1:
                            if inp[k-count].find(")") != -1:
                                count += 2
                            else:
                                inp[k-count] = "(" + inp[k-count]
                                break
                        count = 1
                        while 1:
                            if inp[k + count].find("(") != -1 and inp[k + count + 1]:
                                count += 2
                            else:
                                inp[k + count] = inp[k + count] + ")"
                                break
                        operations["-"].pop(0)

        elif len(operations["+"]) == 0:
            if len(operations["+"]) + len(operations["-"]) > 1:
                j = 0
                for k in operations["+"]:
                    count = 1
                    while 1:
                        if inp[k - count].find(")") != -1:
                            count += 2
                        else:
                            inp[k - count] = "(" + inp[k - count]
                            break
                    count = 1
                    while 1:
                        if inp[k + count].find("(") != -1:
                            count += 2
                        else:
                            inp[k + count] = inp[k + count] + ")"
                            break
                    operations["-"].pop(0)
        elif len(operations["-"]) == 0:
            if len(operations["+"]) + len(operations["-"]) > 1:
                k = 0
                for j in operations["+"]:
                    count = 1
                    while 1:
                        if inp[j - count].find(")") != -1:
                            count += 2
                        else:
                            inp[j - count] = "(" + inp[j - count]
                            break
                    count = 1
                    while 1:
                        if inp[j + count].find("(") != -1:
                            count += 2
                        else:
                            inp[j + count] = inp[j + count] + ")"
                            break
                    operations["+"].pop(0)
    print(" ".join(inp))

# 8
# 1 + 2
# 1 + 2 X 3
# 1 X 2 + 3 X 4 + 5
# 1 + 2 X 3 - 4
# 1 - 2 X 3 X 4
# 1 X 2 X 3 X 4 X 5 X 6 X 7 X 8 X 9
# 1 - 2 X 3 X 4 X 5 + 6 X 7 X 8 - 9 *************************
# 1 X 1 + 1 X 1 + 1 X 1



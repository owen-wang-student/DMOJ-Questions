n = int(input())
for i in range(n):
    inp = input()
    temp = []
    for j in range(2, len(inp)):
        if j-1 == int(inp[0]):
            pass
        else:
            temp.append(inp[j])

    print(i+1, "".join(temp))

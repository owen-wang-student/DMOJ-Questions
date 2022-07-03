def comb(maxLen, current, numOnes):
    if len(current) == maxLen and current.count("1") == numOnes:
        print(current)
        return
    elif len(current) == maxLen and current.count("1") != numOnes:
        return
    else:
        if current.count("1") < numOnes:
            comb(maxLen, current+"1", numOnes)
        comb(maxLen, current + "0", numOnes)


n = int(input())
for i in range(n):
    inp = list(map(int, input().split()))
    totalDigits = inp[0]
    numOnes = inp[1]
    print("The bit patterns are")
    comb(totalDigits, "", numOnes)
    print()

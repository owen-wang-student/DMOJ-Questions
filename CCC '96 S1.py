def sumFactors(num):
    factors = [1]
    for i in range(2, num):
        if num%i == 0:
            factors.append(i)
    # print(num, ":", factors)
    return sum(factors)


n = int(input())

for i in range(n):
    num = int(input())
    sumF = sumFactors(num)

    if num < sumF:
        print(num, "is an abundant number.")
    elif num > sumF:
        print(num, "is a deficient number.")
    else:
        print(num, "is a perfect number.")
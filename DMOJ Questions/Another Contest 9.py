# Q1

n = int(input())

for i in range(n):
    set1 = []
    set2 = []
    distances = list(map(int, input().split()))

    for j in range(4):
        for k in range(4):
            if j == k:
                pass
            else:
                if distances[j]+distances[k] not in set1:
                    set1.append(distances[j]+distances[k])
                    set2.append(distances[j]+distances[k])
    set2.reverse()
    print(len(set1))
    for j in range(len(set1)):
        print(set1[j], set2[j])


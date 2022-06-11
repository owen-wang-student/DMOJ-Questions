n = int(input())
answers = []
right = 0
for i in range(n):
    answers.append(input())
for i in answers:
    if input() == i:
        right += 1
print(right)
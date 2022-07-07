phonebook = {}

n = int(input())
# Initialize phone book
for i in range(n):
    inp = input().split()
    phonebook[int(inp[1])] = inp[0]

n = int(input())
# Get phone numbers
numbers = []
inside = []
count = [0]*n
for i in range(n):
    number = int(input())
    numbers.append(number)
    if number in inside:
        count[numbers.index(number)] = count[numbers.index(number)] + 1
    elif phonebook[number]:
        inside.append(number)
        count[numbers.index(number)] = count[numbers.index(number)] + 1

# Get final
maxx = 0
possible = []
for i in range(len(count)):
    if count[i] > maxx:
        possible.clear()
        possible.append(numbers[i])
        maxx = count[i]
    elif count[i] == maxx:
        possible.append(numbers[i])

possible.sort()
print(phonebook[possible[0]])













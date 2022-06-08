n = int(input())
words = {}
code = []

for i in range(n):
    letter = input().split()
    words[letter[1]] = letter[0]

encoding = input()
for i in encoding:
    code.append(i)

FINALMESSAGE = ""
string = ""
for i in code:
    string += i
    if string in words:
        FINALMESSAGE += words[string]
        string = ""

print(FINALMESSAGE)
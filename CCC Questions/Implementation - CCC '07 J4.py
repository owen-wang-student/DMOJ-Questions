a = input().split()
b = input().split()

word1 = ""
word2 = ""

list1 = []
list2 = []

for i in a: word1 += i
for i in b: word2 += i

for i in word1: list1.append(i)
for i in word2: list2.append(i)

list1.sort()
list2.sort()

if list1 == list2:
    print("Is an anagram.")
else:
    print("Is not an anagram.")
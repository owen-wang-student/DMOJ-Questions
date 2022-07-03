def is_palindrome(word):
    if len(word) == 2:
        if word.count(word[0]) == 2:
            return True
        else:
            return False
    else:
        for i in range(len(word)//2):
            if word[i] != word[(-1*i)-1]:
                return False
        return True


lengths = [1]
word = input()
for i in range(2, len(word)+1):
    start = 0
    for j in range(len(word)-i+1):
        temp = word[start:start+i]
        if is_palindrome(temp):
            lengths.append(len(temp))
        start += 1
        if start >= len(word):
            break

print(max(lengths))
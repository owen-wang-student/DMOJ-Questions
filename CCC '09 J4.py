def addPeriod(maxChar, sentence):
    if len(sentence) == 1:
        sentence.append((maxChar - len(sentence[0]))*".")
    else:
        needed = maxChar
        numPeriod = len(sentence)//2
        for i in sentence:
            needed -= len(i)
        counter = 1

        if numPeriod == 1:
            for i in range(needed):
                current = sentence[counter]
                current += "."
                sentence[counter] = current
        else:
            for i in range(needed):
                current = sentence[counter]
                current += "."
                sentence[counter] = current
                counter += 2
                if counter == len(sentence):
                    counter = 1
    return sentence


words = ["WELCOME", "TO", "CCC", "GOOD", "LUCK", "TODAY"]

sentence = []
output = []
maxChar = int(input())

currentLength = 0
counter = 0

while "pp big":
    sentence.append(words[counter])
    currentLength += len(words[counter])
    counter += 1
    if counter > 5:
        break
    if currentLength + len(words[counter]) + 1 <= maxChar:
        currentLength += 1
        sentence.append(".")
    else:
        sentence = addPeriod(maxChar, sentence)

        output.append(sentence)
        sentence = []
        currentLength = 0

sentence = addPeriod(maxChar, sentence)
output.append(sentence)

for i in output:
    print("".join(i))
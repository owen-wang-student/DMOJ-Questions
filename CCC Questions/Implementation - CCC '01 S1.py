hand = input()

cp = dp = hp = sp = 0
c = d = h = s = False
clubs = []
diamonds = []
hearts = []
spades = []

for i in hand:
    if i == "C":
        c = True
        d = False
        h = False
        s = False
    elif i == "D":
        d = True
        c = False
        h = False
        s = False
    elif i == "H":
        h = True
        d = False
        c = False
        s = False
    elif i == "S":
        s = True
        d = False
        h = False
        c = False

    if c and i != "C":
        clubs.append(i)
    elif d and i != "D":
        diamonds.append(i)
    elif h and i != "H":
        hearts.append(i)
    elif s and i != "S":
        spades.append(i)

for i in clubs:
    if i == "A":
        cp += 4
    elif i == "K":
        cp += 3
    elif i == "Q":
        cp += 2
    elif i == "J":
        cp += 1
if len(clubs) == 0:
    cp += 3
elif len(clubs) == 1:
    cp += 2
elif len(clubs) == 2:
    cp += 1
for i in diamonds:
    if i == "A":
        dp += 4
    elif i == "K":
        dp += 3
    elif i == "Q":
        dp += 2
    elif i == "J":
        dp += 1
if len(diamonds) == 0:
    dp += 3
elif len(diamonds) == 1:
    dp += 2
elif len(diamonds) == 2:
    dp += 1
for i in hearts:
    if i == "A":
        hp += 4
    elif i == "K":
        hp += 3
    elif i == "Q":
        hp += 2
    elif i == "J":
        hp += 1
if len(hearts) == 0:
    hp += 3
elif len(hearts) == 1:
    hp += 2
elif len(hearts) == 2:
    hp += 1
for i in spades:
    if i == "A":
        sp += 4
    elif i == "K":
        sp += 3
    elif i == "Q":
        sp += 2
    elif i == "J":
        sp += 1
if len(spades) == 0:
    sp += 3
elif len(spades) == 1:
    sp += 2
elif len(spades) == 2:
    sp += 1

print("Cards Dealt              Points")
print("Clubs", " ".join(clubs), "\t\t", cp)
print("Diamonds", " ".join(diamonds), "\t\t", dp)
print("Hearts", " ".join(hearts), "\t\t", hp)
print("Spades", " ".join(spades), "\t\t", sp)
print("\t\tTotal", cp+dp+hp+sp)


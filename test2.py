hand = input()

cp = dp = hp = sp = 0
c = d = h = s = False
clubs = diamonds = hearts = spades = []

for i in hand:
    if i == "C":
        c = True
        d = h = s = False
    elif i == "D":
        d = True
        c = h = s = False
    elif i == "H":
        h = True
        d = c = s = False
    elif i == "S":
        s = True
        d = h = c = False

    if c and i != "C":
        clubs.append(i)
    if d and i != "D":
        diamonds.append(i)
    if h and i != "H":
        hearts.append(i)
    if s and i != "S":
        spades.append(i)

print("Cards Dealt              Points")
print("Clubs", " ".join(clubs))
print("Diamonds", " ".join(diamonds))
print("Hearts", " ".join(hearts))
print("Spades", " ".join(spades))


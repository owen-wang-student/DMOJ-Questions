deck = []
big = ["ace", "king", "queen", "jack"]
value = {"ace": 4,
         "king": 3,
         "queen": 2,
         "jack": 1
         }

a = 0
b = 0

for i in range(52):
    deck.append(input())

for i in range(len(deck)):
    card = deck[i]
    cond = True

    if card == "ace" and i+4 < 52:
        for j in range(1,5):
            if deck[i+j] in big:
                cond = False
    elif card == "king" and i+3 < 52:
        for j in range(1,4):
            if deck[i+j] in big:
                cond = False
    elif card == "queen" and i+2 < 52:
        for j in range(1,3):
            if deck[i+j] in big:
                cond = False
    elif card == "jack" and i+1 < 52:
        if deck[i + 1] in big:
            cond = False
    else:
        cond = False

    if cond:
        if i%2 == 0:
            a += value[card]
            print("Player A scores", value[card], "point(s).")
        else:
            b += value[card]
            print("Player B scores", value[card], "point(s).")

print("Player A:", a, "point(s).")
print("Player B:", b, "point(s).")



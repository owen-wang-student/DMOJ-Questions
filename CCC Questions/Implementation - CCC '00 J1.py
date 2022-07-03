start, total = list(map(int, input().split()))

# First Line
print("Sun Mon Tue Wed Thr Fri Sat")

# First Number
print("  ", end="")
if start == 1:
    print(1,end="")
else:
    print("   "+"    "*(start-2), 1, end="")

# First Number Line
current = 1
for i in range(2, 7-start+2):
    print("  ", i, end="")
    current = i
print()

# Remaining Number Line
c = 0
for i in range(current+1, total+1):
    if c == 0 and i < 10:
        print("  ", end="")
    elif c == 0 and i >= 10:
        print(" ",end="")
    elif i < 10:
        print("   ", end="")
    else:
        print("  ",end="")
    print(i, end="")

    c += 1
    if c == 7:
        c = 0
        print()

# If calender doesnt end on saturday
if c != 0:
    print()






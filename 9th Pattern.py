for i in range(6):
    for a in range(6 - i - 1):
        print(" ", end='')
    for b in range(2 * i + 1):
        print("*", end='')
    for c in range(6 - i - 1):
        print(" ", end='')
    print()

for j in range(6):
    for d in range(j):
        print(" " ,end='')
    for e in range(2 * 5 - (2 * j - 1)):
        print("*", end="")
    for f in range(j):
        print(" ", end='')
    print()
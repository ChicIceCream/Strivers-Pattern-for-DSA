for i in range(6):
    for j in range(6 - i - 1):
        print(" ", end='')
    for k in range(2 * i + 1):
        print("*", end='')
    for l in range(6 - i - 1):
        print(" ", end='')
    print()
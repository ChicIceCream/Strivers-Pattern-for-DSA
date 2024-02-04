def func1(n):
    i = n
    while i >= 0:
        print("*" * i)
        i -= 1

def func2(n):
    for i in range(n):
        for j in range(0, n-i):
            print("*", end='')
        print()

print(func2(5))
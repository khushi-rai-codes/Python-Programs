n = 5
for i in range(1, n + 1):
    for j in range(i, n):
        print(" ", end="")
    for j in range(1, 2 * i):
        if j == 1 or j == (2 * i - 1) or i == n:
            print(i, end="")
        else:
            print(" ", end="")
    print()

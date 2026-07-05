n = 5
for i in range(n, 0, -1):
    for j in range(n - i):
        print(" ", end="")
    for ch in range(ord('A'), ord('A') + i):
        print(chr(ch), end="")
    print()
for i in range(2, n + 1):
    for j in range(n - i):
        print(" ", end="")
    for ch in range(ord('A'), ord('A') + i):
        print(chr(ch), end="")
    print()

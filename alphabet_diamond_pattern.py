n = 5
for i in range(n):
    for j in range(i, n - 1):
        print(" ", end="")
    for ch in range(ord('A'), ord('A') + i + 1):
        print(chr(ch), end="")
    for ch in range(ord('A') + i - 1, ord('A') - 1, -1):
        print(chr(ch), end="")
    print()
for i in range(n - 2, -1, -1):
    for j in range(n - 1, i, -1):
        print(" ", end="")
    for ch in range(ord('A'), ord('A') + i + 1):
        print(chr(ch), end="")
    for ch in range(ord('A') + i - 1, ord('A') - 1, -1):
        print(chr(ch), end="")
    print()

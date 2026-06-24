n = 5
num = 1
for i in range(1, n + 1):
    if i % 2 == 1:
        for j in range(i):
            print(num, end=" ")
            num += 1
    else:
        start = num + i - 1
        for j in range(start, num - 1, -1):
            print(j, end=" ")
        num += i
    print()

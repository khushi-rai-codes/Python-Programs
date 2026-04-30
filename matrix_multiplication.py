r1 = int(input("Enter rows of first matrix: "))
c1 = int(input("Enter columns of first matrix: "))
r2 = int(input("Enter rows of second matrix: "))
c2 = int(input("Enter columns of second matrix: "))
if c1 != r2:
    print("Matrix multiplication not possible")
else:
    a = []
    b = []
    result = [[0 for _ in range(c2)] for _ in range(r1)]
    print("Enter first matrix:")
    for i in range(r1):
        row = list(map(int, input().split()))
        a.append(row)
    print("Enter second matrix:")
    for i in range(r2):
        row = list(map(int, input().split()))
        b.append(row)
    for i in range(r1):
        for j in range(c2):
            for k in range(c1):
                result[i][j] += a[i][k] * b[k][j]
    print("Resultant matrix:")
    for row in result:
        print(*row)

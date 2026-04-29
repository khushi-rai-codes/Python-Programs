rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
matrix = []
print("Enter matrix elements:")
for i in range(rows):
    row = list(map(int, input().split()))
    matrix.append(row)
print("Transpose matrix:")
for i in range(cols):
    for j in range(rows):
        print(matrix[j][i], end=" ")
    print()

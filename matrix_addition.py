rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
a = []
b = []
sum_matrix = []
print("Enter elements of first matrix:")
for i in range(rows):
    row = list(map(int, input().split()))
    a.append(row)
print("Enter elements of second matrix:")
for i in range(rows):
    row = list(map(int, input().split()))
    b.append(row)
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(a[i][j] + b[i][j])
    sum_matrix.append(row)
print("Resultant matrix:")
for row in sum_matrix:
    print(*row)

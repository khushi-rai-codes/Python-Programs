n = int(input("Enter size of square matrix: "))
matrix = []
print("Enter matrix elements:")
for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)
sum_diagonal = 0
for i in range(n):
    sum_diagonal += matrix[i][i]
print("Primary diagonal sum =", sum_diagonal)

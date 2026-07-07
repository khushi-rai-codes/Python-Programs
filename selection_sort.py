n = int(input("Enter number of elements: "))
arr = []
print("Enter elements:")
for _ in range(n):
    arr.append(int(input()))
for i in range(n - 1):
    minimum = i
    for j in range(i + 1, n):
        if arr[j] < arr[minimum]:
            minimum = j
    arr[i], arr[minimum] = arr[minimum], arr[i]
print("Sorted array:")
for i in arr:
    print(i, end=" ")

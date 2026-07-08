n = int(input("Enter number of elements: "))
arr = list(map(int, input("Enter array elements: ").split()))
d = int(input("Enter number of left rotations: "))
d = d % n
rotated = arr[d:] + arr[:d]
print("Array after rotation:")
print(*rotated)

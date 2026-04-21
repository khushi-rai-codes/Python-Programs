arr = []
print("Enter 5 numbers:")
for i in range(5):
    num = int(input())
    arr.append(num)
largest = arr[0]
for i in arr:
    if i > largest:
        largest = i
print("Largest number =", largest)

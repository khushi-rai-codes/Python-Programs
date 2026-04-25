num = int(input("Enter a number: "))
sum = 0
while num != 0:
    remainder = num % 10
    sum = sum + remainder
    num = num // 10
print("Sum of digits =", sum)

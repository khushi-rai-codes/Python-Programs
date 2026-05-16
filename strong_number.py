def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact
num = int(input("Enter a number: "))
original = num
sum_digits = 0
while num > 0:
    digit = num % 10
    sum_digits += factorial(digit)
    num //= 10
if sum_digits == original:
    print(original, "is a Strong Number")
else:
    print(original, "is not a Strong Number")

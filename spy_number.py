num = int(input("Enter a number: "))
temp = num
sum_digits = 0
product_digits = 1
while temp > 0:
    digit = temp % 10
    sum_digits += digit
    product_digits *= digit
    temp //= 10
if sum_digits == product_digits:
    print(num, "is a Spy Number")
else:
    print(num, "is not a Spy Number")

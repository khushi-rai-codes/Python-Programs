num = int(input("Enter a number: "))
original = num
result = 0
while num != 0:
    remainder = num % 10
    result = result + (remainder ** 3)
    num = num // 10
if original == result:
    print("Armstrong number")
else:
    print("Not an Armstrong number")

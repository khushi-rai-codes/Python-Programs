numbers = []

n = int(input("How many numbers? "))

for i in range(n):
    number = int(input(f"Enter number {i + 1}: "))
    numbers.append(number)

if n > 0:
    largest = numbers[0]

    for number in numbers:
        if number > largest:
            largest = number

    print("Largest number:", largest)
else:
    print("No numbers entered.")

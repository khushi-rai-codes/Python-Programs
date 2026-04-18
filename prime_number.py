n = int(input("Enter a number: "))
if n <= 1:
    print("Not a prime number")
else:
    flag = 0
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            flag = 1
            break
    if flag == 0:
        print("Prime number")
    else:
        print("Not a prime number")

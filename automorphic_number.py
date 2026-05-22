num = int(input("Enter a number: "))
square = num * num
digits = len(str(num))
if square % (10 ** digits) == num:
    print(num, "is an Automorphic Number")
else:
    print(num, "is not an Automorphic Number")

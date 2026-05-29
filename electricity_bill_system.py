units = int(input("Enter electricity units consumed: "))
if units <= 100:
    bill = units * 1.5
elif units <= 300:
    bill = (100 * 1.5) + ((units - 100) * 2.5)
else:
    bill = (100 * 1.5) + (200 * 2.5) + ((units - 300) * 4)
print("Total Electricity Bill =", bill)

import csv
filename = "expenses.csv"
date = input("Enter Date (DD-MM-YYYY): ")
category = input("Enter Category: ")
amount = float(input("Enter Amount: "))
with open(filename, "a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow([date, category, amount])
print("\nExpense Saved Successfully!")

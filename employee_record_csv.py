import csv
employee_id = int(input("Enter Employee ID: "))
name = input("Enter Employee Name: ")
salary = float(input("Enter Salary: "))
with open("employees.csv", "a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow([employee_id, name, salary])
print("Employee record saved successfully.")

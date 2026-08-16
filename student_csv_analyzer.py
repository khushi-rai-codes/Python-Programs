import csv
filename = "students.csv"
students = []
try:
    with open(filename, "r", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            row["marks"] = float(row["marks"])
            students.append(row)
except FileNotFoundError:
    print("students.csv file not found.")
    exit()
if not students:
    print("No student records found.")
    exit()
highest = max(students, key=lambda student: student["marks"])
average = sum(student["marks"] for student in students) / len(students)
print("\n----- Student Analysis -----")
print("Number of Students:", len(students))
print("Average Marks:", round(average, 2))
print(
    "Highest Marks:",
    highest["name"],
    "-",
    highest["marks"]
)

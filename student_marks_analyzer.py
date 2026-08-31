import csv
filename = input("Enter CSV file name: ")
students = []
try:
    with open(filename, "r", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            name = row["Name"]
            marks = float(row["Marks"])
            students.append({
                "Name": name,
                "Marks": marks
            })
    if not students:
        print("No student records found.")
    else:
        print("\n===== STUDENT MARKS =====")
        total = 0
        for student in students:
            print(
                f"{student['Name']} : "
                f"{student['Marks']}"
            )
            total += student["Marks"]
        average = total / len(students)
        highest = max(
            students,
            key=lambda student: student["Marks"]
        )
        print("\nAverage Marks:", round(average, 2))
        print(
            "Highest Marks:",
            highest["Name"],
            "-",
            highest["Marks"]
        )
except FileNotFoundError:
    print("File not found.")
except KeyError:
    print("CSV must contain 'Name' and 'Marks' columns.")
except ValueError:
    print("Marks must contain valid numbers.")

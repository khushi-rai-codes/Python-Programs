student = {}
student["Roll Number"] = int(input("Enter Roll Number: "))
student["Name"] = input("Enter Name: ")
student["Marks"] = float(input("Enter Marks: "))
print("\n----- Student Details -----")
for key, value in student.items():
    print(f"{key} : {value}")

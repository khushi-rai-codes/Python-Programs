import json
student = {
    "roll": int(input("Enter Roll Number: ")),
    "name": input("Enter Name: "),
    "marks": float(input("Enter Marks: "))
}
with open("student.json", "w") as file:
    json.dump(student, file, indent=4)
print("Student record saved successfully.")

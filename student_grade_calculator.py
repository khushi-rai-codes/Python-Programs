def calculate_grade(marks):
    average = sum(marks) / len(marks)

    if average >= 90:
        grade = "A+"
    elif average >= 80:
        grade = "A"
    elif average >= 70:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 50:
        grade = "D"
    else:
        grade = "F"

    return average, grade


subjects = int(input("Enter number of subjects: "))

marks = []

for i in range(subjects):
    mark = float(input(f"Enter marks for subject {i + 1}: "))

    if 0 <= mark <= 100:
        marks.append(mark)
    else:
        print("Invalid marks. Enter a value between 0 and 100.")
        break
else:
    average, grade = calculate_grade(marks)

    print("\n===== RESULT =====")
    print(f"Total Marks: {sum(marks):.2f}")
    print(f"Average: {average:.2f}")
    print(f"Grade: {grade}")

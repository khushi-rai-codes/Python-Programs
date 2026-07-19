name = input("Enter Student Name: ")
marks = []
for i in range(5):
    marks.append(int(input(f"Enter Marks of Subject {i+1}: ")))
total = sum(marks)
average = total / 5
if average >= 90:
    grade = "A+"
elif average >= 75:
    grade = "A"
elif average >= 60:
    grade = "B"
elif average >= 40:
    grade = "C"
else:
    grade = "Fail"
print("\n----- Report Card -----")
print("Name :", name)
print("Total :", total)
print("Average :", average)
print("Grade :", grade)

marks = float(input("Enter marks out of 100: "))
percentage = marks
print("Percentage =", percentage)
if percentage >= 90:
    print("Grade A")
elif percentage >= 75:
    print("Grade B")
elif percentage >= 60:
    print("Grade C")
elif percentage >= 40:
    print("Grade D")
else:
    print("Fail")

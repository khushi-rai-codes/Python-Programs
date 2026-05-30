students = []
while True:
    print("\n1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Exit")
    choice = int(input("Enter Choice: "))
    if choice == 1:
        roll = int(input("Enter Roll Number: "))
        name = input("Enter Name: ")
        students.append((roll, name))
        print("Student Added Successfully")
    elif choice == 2:
        if len(students) == 0:
            print("No Students Found")
        for roll, name in students:
            print("Roll:", roll)
            print("Name:", name)
    elif choice == 3:
        roll = int(input("Enter Roll Number: "))
        found = False
        for r, name in students:
            if r == roll:
                print("Student Found")
                print("Name:", name)
                found = True
                break
        if not found:
            print("Student Not Found")
    elif choice == 4:
        break

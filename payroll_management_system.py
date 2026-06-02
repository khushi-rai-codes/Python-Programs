employees = []
while True:
    print("\n1. Add Employee")
    print("2. Display Employees")
    print("3. Search Employee")
    print("4. Exit")
    choice = int(input("Enter Choice: "))
    if choice == 1:
        emp_id = int(input("Enter Employee ID: "))
        name = input("Enter Employee Name: ")
        salary = float(input("Enter Salary: "))
        employees.append((emp_id, name, salary))
        print("Employee Added Successfully")
    elif choice == 2:
        if len(employees) == 0:
            print("No Employees Found")
        for emp_id, name, salary in employees:
            print("ID:", emp_id)
            print("Name:", name)
            print("Salary:", salary)
    elif choice == 3:
        emp_id = int(input("Enter Employee ID: "))
        found = False
        for eid, name, salary in employees:
            if eid == emp_id:
                print("Employee Found")
                print("Name:", name)
                print("Salary:", salary)
                found = True
                break
        if not found:
            print("Employee Not Found")
    elif choice == 4:
        break

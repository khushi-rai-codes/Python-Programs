courses = []
while True:
    print("\n1. Add Course")
    print("2. Display Courses")
    print("3. Search Course")
    print("4. Exit")
    choice = int(input("Enter Choice: "))
    if choice == 1:
        course_id = int(input("Enter Course ID: "))
        name = input("Enter Course Name: ")
        courses.append((course_id, name))
        print("Course Added Successfully")
    elif choice == 2:
        if len(courses) == 0:
            print("No Courses Found")
        for cid, name in courses:
            print("ID:", cid)
            print("Name:", name)
    elif choice == 3:
        course_id = int(input("Enter Course ID: "))
        found = False
        for cid, name in courses:
            if cid == course_id:
                print("Course Found")
                print("Name:", name)
                found = True
                break
        if not found:
            print("Course Not Found")
    elif choice == 4:
        break

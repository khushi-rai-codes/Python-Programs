patients = []
while True:
    print("\n1. Add Patient")
    print("2. Display Patients")
    print("3. Search Patient")
    print("4. Exit")
    choice = int(input("Enter Choice: "))
    if choice == 1:
        patient_id = int(input("Enter Patient ID: "))
        name = input("Enter Patient Name: ")
        patients.append((patient_id, name))
        print("Patient Added Successfully")
    elif choice == 2:
        if len(patients) == 0:
            print("No Patients Found")
        for pid, name in patients:
            print("ID:", pid)
            print("Name:", name)
    elif choice == 3:
        patient_id = int(input("Enter Patient ID: "))
        found = False
        for pid, name in patients:
            if pid == patient_id:
                print("Patient Found")
                print("Name:", name)
                found = True
                break
        if not found:
            print("Patient Not Found")
    elif choice == 4:
        break

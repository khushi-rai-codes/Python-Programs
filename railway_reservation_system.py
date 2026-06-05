passengers = []
while True:
    print("\n1. Book Ticket")
    print("2. View Reservations")
    print("3. Search Passenger")
    print("4. Cancel Ticket")
    print("5. Exit")
    choice = int(input("Enter Choice: "))
    if choice == 1:
        pid = int(input("Enter Passenger ID: "))
        name = input("Enter Passenger Name: ")
        passengers.append((pid, name))
        print("Ticket Booked Successfully")
    elif choice == 2:
        if len(passengers) == 0:
            print("No Reservations Found")
        for pid, name in passengers:
            print("ID:", pid)
            print("Name:", name)
    elif choice == 3:
        pid = int(input("Enter Passenger ID: "))
        found = False
        for p, name in passengers:
            if p == pid:
                print("Passenger Found")
                print("Name:", name)
                found = True
                break
        if not found:
            print("Passenger Not Found")
    elif choice == 4:
        pid = int(input("Enter Passenger ID to Cancel: "))
        for i in range(len(passengers)):
            if passengers[i][0] == pid:
                passengers.pop(i)
                print("Reservation Cancelled")
                break
        else:
            print("Passenger Not Found")
    elif choice == 5:
        break

seats = [0] * 10
while True:
    print("\n1. View Seats")
    print("2. Book Seat")
    print("3. Cancel Seat")
    print("4. Exit")
    choice = int(input("Enter Choice: "))
    if choice == 1:
        for i in range(10):
            status = "Booked" if seats[i] else "Available"
            print(f"Seat {i+1}: {status}")
    elif choice == 2:
        seat = int(input("Enter Seat Number (1-10): "))
        if 1 <= seat <= 10 and seats[seat-1] == 0:
            seats[seat-1] = 1
            print("Seat Booked")
        else:
            print("Invalid/Already Booked")
    elif choice == 3:
        seat = int(input("Enter Seat Number (1-10): "))
        if 1 <= seat <= 10 and seats[seat-1] == 1:
            seats[seat-1] = 0
            print("Booking Cancelled")
        else:
            print("Seat Not Booked")
    elif choice == 4:
        break

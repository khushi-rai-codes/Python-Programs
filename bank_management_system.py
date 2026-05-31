account_number = int(input("Enter Account Number: "))
balance = 0
while True:
    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")
    choice = int(input("Enter Choice: "))
    if choice == 1:
        amount = float(input("Enter Amount: "))
        balance += amount
    elif choice == 2:
        amount = float(input("Enter Amount: "))
        if amount <= balance:
            balance -= amount
        else:
            print("Insufficient Balance")
    elif choice == 3:
        print("Balance =", balance)
    elif choice == 4:
        break

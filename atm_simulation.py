balance = 1000
while True:
    print("\n--- ATM MENU ---")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        print("Current Balance =", balance)
    elif choice == 2:
        amount = float(input("Enter amount to deposit: "))
        balance += amount
        print("Amount Deposited Successfully")
    elif choice == 3:
        amount = float(input("Enter amount to withdraw: "))
        if amount > balance:
            print("Insufficient Balance")
        else:
            balance -= amount
            print("Please collect your cash")
    elif choice == 4:
        print("Thank you for using ATM")
        break
    else:
        print("Invalid Choice")

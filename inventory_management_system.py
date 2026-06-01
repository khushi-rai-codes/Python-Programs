items = []
while True:
    print("\n1. Add Item")
    print("2. Display Items")
    print("3. Search Item")
    print("4. Exit")
    choice = int(input("Enter Choice: "))
    if choice == 1:
        item_id = int(input("Enter Item ID: "))
        name = input("Enter Item Name: ")
        items.append((item_id, name))
        print("Item Added Successfully")
    elif choice == 2:
        if len(items) == 0:
            print("No Items Available")
        for item_id, name in items:
            print("ID:", item_id)
            print("Name:", name)
    elif choice == 3:
        item_id = int(input("Enter Item ID: "))
        found = False
        for i, n in items:
            if i == item_id:
                print("Item Found")
                print("Name:", n)
                found = True
                break
        if not found:
            print("Item Not Found")
    elif choice == 4:
        break

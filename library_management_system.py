books = []
while True:
    print("\n--- LIBRARY MENU ---")
    print("1. Add Book")
    print("2. Display Books")
    print("3. Search Book")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        name = input("Enter book name: ")
        books.append(name)
        print("Book added successfully")
    elif choice == 2:
        if len(books) == 0:
            print("No books available")
        else:
            print("Books in Library:")
            for i in range(len(books)):
                print(i + 1, ".", books[i])
    elif choice == 3:
        name = input("Enter book name to search: ")
        if name in books:
            print("Book Found")
        else:
            print("Book Not Found")
    elif choice == 4:
        print("Exiting Program")
        break
    else:
        print("Invalid Choice")

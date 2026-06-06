books = []
while True:
    print("\n1. Add Book")
    print("2. Display Books")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Exit")
    choice = int(input("Enter Choice: "))
    if choice == 1:
        book_id = int(input("Enter Book ID: "))
        title = input("Enter Book Title: ")
        books.append({
            "id": book_id,
            "title": title,
            "issued": False
        })
        print("Book Added Successfully")
    elif choice == 2:
        for book in books:
            print("ID:", book["id"])
            print("Title:", book["title"])
            print("Status:",
                  "Issued" if book["issued"]
                  else "Available")
    elif choice == 3:
        book_id = int(input("Enter Book ID: "))
       for book in books:
            if book["id"] == book_id:
                book["issued"] = True
                print("Book Issued")
                break
    elif choice == 4:
        book_id = int(input("Enter Book ID: "))
        for book in books:
            if book["id"] == book_id:
                book["issued"] = False
                print("Book Returned")
                break
    elif choice == 5:
        break

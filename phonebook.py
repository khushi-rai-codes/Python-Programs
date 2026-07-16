phonebook = {}
n = int(input("Enter number of contacts: "))
for i in range(n):
    name = input("Enter Name: ")
    number = input("Enter Phone Number: ")
    phonebook[name] = number
print("\nPhone Book")
for name, number in phonebook.items():
    print(f"{name} : {number}")

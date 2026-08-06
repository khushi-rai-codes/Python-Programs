import json
contact = {
    "name": input("Enter Name: "),
    "phone": input("Enter Phone Number: "),
    "email": input("Enter Email: ")
}
with open("contacts.json", "w") as file:
    json.dump(contact, file, indent=4)
print("Contact saved successfully.")

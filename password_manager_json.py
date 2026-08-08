import json
import os
FILE_NAME = "passwords.json"
def load_passwords():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return {}
def save_passwords(passwords):
    with open(FILE_NAME, "w") as file:
        json.dump(passwords, file, indent=4)
def add_password(passwords):
    website = input("Enter Website: ")
    username = input("Enter Username: ")
    password = input("Enter Password: ")
    passwords[website] = {
        "username": username,
        "password": password
    }
    save_passwords(passwords)
    print("Password saved successfully.")
def view_passwords(passwords):
    if not passwords:
        print("No passwords saved.")
        return
    print("\n----- Saved Passwords -----")
    for website, details in passwords.items():
        print("Website :", website)
        print("Username:", details["username"])
        print("Password:", details["password"])
        print()
def main():
    passwords = load_passwords()
    while True:
        print("\n===== Password Manager =====")
        print("1. Add Password")
        print("2. View Passwords")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_password(passwords)
        elif choice == "2":
            view_passwords(passwords)
        elif choice == "3":
            print("Exiting Password Manager.")
            break
        else:
            print("Invalid choice.")
if __name__ == "__main__":
    main()

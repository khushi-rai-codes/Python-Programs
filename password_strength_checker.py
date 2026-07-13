import string
password = input("Enter Password: ")
strength = 0
if len(password) >= 8:
    strength += 1
if any(c.isupper() for c in password):
    strength += 1
if any(c.islower() for c in password):
    strength += 1
if any(c.isdigit() for c in password):
    strength += 1
if any(c in string.punctuation for c in password):
    strength += 1
levels = {
    5: "Very Strong",
    4: "Strong",
    3: "Medium",
    2: "Weak",
    1: "Very Weak",
    0: "Very Weak"
}
print("Password Strength:", levels[strength])

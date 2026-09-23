def caesar_cipher(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            encrypted = chr((ord(char) - base + shift) % 26 + base)
            result += encrypted
        else:
            result += char

    return result


text = input("Enter text: ")
shift = int(input("Enter shift value: "))

encrypted_text = caesar_cipher(text, shift)

print("Encrypted text:", encrypted_text)

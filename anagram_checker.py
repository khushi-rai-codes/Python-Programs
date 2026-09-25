def normalize(text):
    return sorted(
        char.lower()
        for char in text
        if char.isalnum()
    )


def are_anagrams(first, second):
    return normalize(first) == normalize(second)


first = input("Enter first string: ")
second = input("Enter second string: ")

if are_anagrams(first, second):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")

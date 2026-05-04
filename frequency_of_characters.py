text = input("Enter a string: ")
freq = {}
for ch in text:
    if ch != " ":
        freq[ch] = freq.get(ch, 0) + 1
print("Character frequencies:")
for ch, count in freq.items():
    print(ch, "=", count)

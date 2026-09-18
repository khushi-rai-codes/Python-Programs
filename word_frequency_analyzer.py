from collections import Counter
import re

text = input("Enter a sentence: ")

words = re.findall(r"\b[a-zA-Z]+\b", text.lower())

frequency = Counter(words)

print("\n===== WORD FREQUENCY =====")

if not frequency:
    print("No words found.")
else:
    for word, count in frequency.most_common():
        print(f"{word}: {count}")

    print("\nTotal words:", len(words))
    print("Unique words:", len(frequency))

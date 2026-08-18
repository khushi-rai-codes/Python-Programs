import os
import hashlib
folder = input("Enter folder path: ")
file_hashes = {}
for root, directories, files in os.walk(folder):
    for filename in files:
        path = os.path.join(root, filename)
        try:
            with open(path, "rb") as file:
                file_hash = hashlib.md5(file.read()).hexdigest()
            if file_hash in file_hashes:
                print("\nDuplicate File Found:")
                print("Original :", file_hashes[file_hash])
                print("Duplicate:", path)
            else:
                file_hashes[file_hash] = path
        except (PermissionError, OSError):
            continue

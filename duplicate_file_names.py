import os
from collections import defaultdict
folder = input("Enter folder path: ")
if not os.path.isdir(folder):
    print("Invalid folder path.")
else:
    files = defaultdict(list)
    for filename in os.listdir(folder):
        full_path = os.path.join(folder, filename)
        if os.path.isfile(full_path):
            files[filename].append(full_path)
    duplicates_found = False
    print("\n===== DUPLICATE FILE NAMES =====")
    for filename, paths in files.items():
        if len(paths) > 1:
            duplicates_found = True
            print("\nFile:", filename)
            for path in paths:
                print(" -", path)
    if not duplicates_found:
        print("No duplicate file names found.")

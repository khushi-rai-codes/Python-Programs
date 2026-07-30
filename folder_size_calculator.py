import os
folder = input("Enter folder path: ")
total_size = 0
for path, dirs, files in os.walk(folder):
    for file in files:
        file_path = os.path.join(path, file)
        if os.path.exists(file_path):
            total_size += os.path.getsize(file_path)
print(f"\nTotal Folder Size: {total_size} bytes")

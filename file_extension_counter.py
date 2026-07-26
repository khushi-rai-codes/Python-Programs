import os
path = input("Enter folder path: ")
extensions = {}
for file in os.listdir(path):
    if os.path.isfile(os.path.join(path, file)):
        ext = os.path.splitext(file)[1]
        if ext == "":
            ext = "No Extension"
        extensions[ext] = extensions.get(ext, 0) + 1
print("\nExtension Count\n")
for ext, count in sorted(extensions.items()):
    print(f"{ext} : {count}")

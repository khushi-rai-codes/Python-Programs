from PIL import Image
import os
filename = input("Enter image file path: ")
if not os.path.exists(filename):
    print("File not found.")
else:
    try:
        image = Image.open(filename)
        width, height = image.size
        print("\n----- Image Information -----")
        print("File Name :", filename)
        print("Format    :", image.format)
        print("Width     :", width, "pixels")
        print("Height    :", height, "pixels")
        print("Mode      :", image.mode)
    except Exception:
        print("Unable to read the image.")

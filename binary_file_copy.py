def copy_binary_file(source, destination):
    try:
        with open(source, "rb") as source_file:
            data = source_file.read()

        with open(destination, "wb") as destination_file:
            destination_file.write(data)

        print("File copied successfully.")

    except FileNotFoundError:
        print("Source file not found.")

    except PermissionError:
        print("Permission denied.")

    except OSError as error:
        print("Error:", error)


source_file = input("Enter source file name: ")
destination_file = input("Enter destination file name: ")

copy_binary_file(source_file, destination_file)

import json


def analyze_json_file(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            data = json.load(file)

        print("\n===== JSON DATA ANALYZER =====")

        if isinstance(data, list):
            print("Data type: List")
            print("Number of records:", len(data))

            if data:
                print("\nFirst record:")
                print(data[0])

        elif isinstance(data, dict):
            print("Data type: Dictionary")
            print("Number of keys:", len(data))

            print("\nKeys:")
            for key in data:
                print("-", key)

        else:
            print("Data type:", type(data).__name__)
            print("Value:", data)

    except FileNotFoundError:
        print("File not found.")

    except json.JSONDecodeError:
        print("Invalid JSON file.")

    except PermissionError:
        print("Permission denied.")

    except OSError as error:
        print("Error:", error)


filename = input("Enter JSON file name: ")
analyze_json_file(filename)

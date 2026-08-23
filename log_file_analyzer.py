from collections import Counter

filename = input("Enter log file name: ")

status_codes = Counter()

try:
    with open(filename, "r") as file:

        for line in file:
            parts = line.split()

            if len(parts) >= 2:
                status_code = parts[-2]
                status_codes[status_code] += 1

    print("\n===== LOG ANALYSIS =====")

    if status_codes:
        for code, count in sorted(status_codes.items()):
            print(f"Status {code}: {count} occurrence(s)")
    else:
        print("No valid log entries found.")

except FileNotFoundError:
    print("File not found.")

except PermissionError:
    print("Permission denied.")

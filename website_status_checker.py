import urllib.request
url = input("Enter website URL: ")p[;'\/
try:
    response = urllib.request.urlopen(url, timeout=5)
    print("\nWebsite is reachable.")
    print("Status Code:", response.status)
except Exception as error:
    print("\nWebsite could not be reached.")
    print("Error:", error)

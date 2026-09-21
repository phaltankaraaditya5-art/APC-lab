employee = {"ID": 18, "Name": "Namo", "Salary": 85000}
key = input("Enter key to search: ")

if key in employee:
    print(employee[key])
else:
    print("Key not found")
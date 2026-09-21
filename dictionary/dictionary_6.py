employees = {101: "Varad", 62: "Shiva", 96: "Pravin"}
emp_id = int(input("Enter employee ID: "))

if emp_id in employees:
    print("Employee exists:", employees[emp_id])
else:
    print("Employee not found")
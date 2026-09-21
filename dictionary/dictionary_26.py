employees = {"Pravin": 45000, "Varad": 60000, "Namo": 30000, "Sartaj": 75000}

highest = max(employees, key=employees.get)
lowest = min(employees, key=employees.get)
average = sum(employees.values()) / len(employees)

print("Highest salary:", highest, "-", employees[highest])
print("Lowest salary:", lowest, "-", employees[lowest])
print("Average salary =", average)

print("Employees earning more than 50000:")
for name, salary in employees.items():
    if salary > 50000:
        print(name, "-", salary)
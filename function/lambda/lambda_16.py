n = int(input("How many employees? "))
employees = []

for i in range(n):
    name = input("Enter employee name: ")
    salary = float(input("Enter salary: "))
    employees.append((name, salary))

sorted_employees = sorted(employees, key=lambda e: e[1])

print("Sorted by salary:", sorted_employees)
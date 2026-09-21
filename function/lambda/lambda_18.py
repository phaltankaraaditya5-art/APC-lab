n = int(input("How many employees? "))
employees = []

for i in range(n):
    name = input("Enter name: ")
    department = input("Enter department: ")
    salary = float(input("Enter salary: "))
    employees.append((name, department, salary))

above_50000 = list(filter(lambda e: e[2] > 50000, employees))
increased_salary = list(map(lambda e: (e[0], e[1], e[2] * 1.10), employees))
sorted_by_salary = sorted(employees, key=lambda e: e[2])

print("Earning more than 50000:", above_50000)
print("After 10% increase:", increased_salary)
print("Sorted by salary:", sorted_by_salary)
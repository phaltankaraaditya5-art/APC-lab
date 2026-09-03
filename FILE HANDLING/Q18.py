def read_employees():
    employees = []

    with open("employees.txt", "r") as file:
        for line in file:
            emp_id, name, department, salary = line.strip().split(",")

            employees.append({
                "id": emp_id,
                "name": name,
                "department": department,
                "salary": float(salary)
            })

    return employees


def display_employees(employees):
    print("Employee Records:")
    for emp in employees:
        print(emp["id"], emp["name"], emp["department"], emp["salary"])


def highest_paid(employees):
    employee = max(employees, key=lambda x: x["salary"])
    print("\nHighest Paid Employee:")
    print(employee["name"], "-", employee["salary"])


def average_salary(employees):
    average = sum(emp["salary"] for emp in employees) / len(employees)
    print("\nAverage Salary:", average)


def above_salary(employees, amount):
    print("\nEmployees earning above", amount)
    for emp in employees:
        if emp["salary"] > amount:
            print(emp["name"], "-", emp["salary"])


employees = read_employees()

display_employees(employees)
highest_paid(employees)
average_salary(employees)

amount = float(input("\nEnter salary limit: "))
above_salary(employees, amount)

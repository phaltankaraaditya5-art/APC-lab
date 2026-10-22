class Employee:
    def calculate_salary(self):
        print("Salary not defined")


class Manager(Employee):
    def calculate_salary(self):
        return 60000


class Developer(Employee):
    def calculate_salary(self):
        return 50000


class Tester(Employee):
    def calculate_salary(self):
        return 40000


employees = [Manager(), Developer(), Tester()]

for emp in employees:
    print("Salary =", emp.calculate_salary())
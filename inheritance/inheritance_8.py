class Employee:
    def __init__(self, emp_id, name, basic_salary):
        self.emp_id = emp_id
        self.name = name
        self.basic_salary = basic_salary


class Manager(Employee):
    def calculate_salary(self):
        return self.basic_salary + 15000


class Developer(Employee):
    def calculate_salary(self):
        return self.basic_salary + 10000


class Tester(Employee):
    def calculate_salary(self):
        return self.basic_salary + 8000


m = Manager("E1", "Rehan", 40000)
d = Developer("E2", "Riya", 35000)
t = Tester("E3", "John", 30000)

print("Manager Salary =", m.calculate_salary())
print("Developer Salary =", d.calculate_salary())
print("Tester Salary =", t.calculate_salary())
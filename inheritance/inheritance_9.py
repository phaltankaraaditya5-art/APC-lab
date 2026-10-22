class Person:
    def __init__(self, name):
        self.name = name


class Student(Person):
    def __init__(self, name, roll_no):
        super().__init__(name)
        self.roll_no = roll_no


class Faculty(Person):
    def __init__(self, name, department):
        super().__init__(name)
        self.department = department


class TeachingAssistant(Student, Faculty):
    def __init__(self, name, roll_no, department):
        Student.__init__(self, name, roll_no)
        Faculty.__init__(self, name, department)

    def display(self):
        print("Name:", self.name)
        print("Roll No:", self.roll_no)
        print("Department:", self.department)


ta = TeachingAssistant("Rehan", "R1", "CSE")
ta.display()
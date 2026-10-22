class Student:
    def __init__(self, roll_no, name, course):
        self.roll_no = roll_no
        self.name = name
        self.course = course


class Result(Student):
    def __init__(self, roll_no, name, course, m1, m2, m3):
        super().__init__(roll_no, name, course)
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def total(self):
        return self.m1 + self.m2 + self.m3

    def percentage(self):
        return (self.total() / 300) * 100

    def grade(self):
        p = self.percentage()
        if p >= 75:
            return "A"
        elif p >= 60:
            return "B"
        else:
            return "C"


result = Result("R1", "Rehan", "CSE", 85, 90, 78)
print("Total =", result.total())
print("Percentage =", result.percentage())
print("Grade =", result.grade())
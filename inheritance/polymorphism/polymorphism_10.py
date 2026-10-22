class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __gt__(self, other):
        return self.marks > other.marks

    def __lt__(self, other):
        return self.marks < other.marks


s1 = Student("Rehan", 85)
s2 = Student("Riya", 90)

if s1 > s2:
    print(s1.name, "scored more")
elif s1 < s2:
    print(s2.name, "scored more")
else:
    print("Both scored equal")
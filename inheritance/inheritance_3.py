class Academic:
    def __init__(self, marks):
        self.marks = marks


class Sports:
    def __init__(self, sports_points):
        self.sports_points = sports_points


class Student(Academic, Sports):
    def __init__(self, name, marks, sports_points):
        Academic.__init__(self, marks)
        Sports.__init__(self, sports_points)
        self.name = name

    def overall_performance(self):
        return (self.marks * 0.7) + (self.sports_points * 0.3)


s = Student("Rehan", 85, 90)
print("Overall Performance =", s.overall_performance())
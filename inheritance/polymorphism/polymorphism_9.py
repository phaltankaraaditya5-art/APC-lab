class Distance:
    def __init__(self, feet, inches):
        self.feet = feet
        self.inches = inches

    def __add__(self, other):
        total_inches = (self.feet*12 + self.inches) + (other.feet*12 + other.inches)
        new_feet = total_inches // 12
        new_inches = total_inches % 12
        return Distance(new_feet, new_inches)

    def display(self):
        print(self.feet, "feet", self.inches, "inches")


d1 = Distance(5, 8)
d2 = Distance(3, 9)

d3 = d1 + d2
d3.display()
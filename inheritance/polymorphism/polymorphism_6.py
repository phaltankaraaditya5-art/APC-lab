class Student:
    def calculate_grade(self, percentage):
        print("Grade not defined")


class EngineeringStudent(Student):
    def calculate_grade(self, percentage):
        if percentage >= 75:
            return "Distinction"
        else:
            return "Pass"


class MedicalStudent(Student):
    def calculate_grade(self, percentage):
        if percentage >= 80:
            return "Distinction"
        else:
            return "Pass"


class ManagementStudent(Student):
    def calculate_grade(self, percentage):
        if percentage >= 70:
            return "Distinction"
        else:
            return "Pass"


students = [EngineeringStudent(), MedicalStudent(), ManagementStudent()]

for s in students:
    print(s.calculate_grade(78))
def average_marks(students):
    total = sum(marks for name, marks in students)
    return total / len(students)

n = int(input("How many students? "))
students = []

for i in range(n):
    name = input("Enter student name: ")
    marks = int(input("Enter marks: "))
    students.append((name, marks))

above_75 = list(filter(lambda s: s[1] > 75, students))
sorted_by_marks = sorted(students, key=lambda s: s[1])

print("Average marks =", average_marks(students))
print("Above 75:", above_75)
print("Sorted:", sorted_by_marks)
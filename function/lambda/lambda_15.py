n = int(input("How many students? "))
students = []

for i in range(n):
    name = input("Enter student name: ")
    marks = int(input("Enter marks: "))
    students.append((name, marks))

sorted_students = sorted(students, key=lambda s: s[1])

print("Sorted by marks:", sorted_students)
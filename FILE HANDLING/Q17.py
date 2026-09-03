
import csv

with open("students.csv", "r") as file:
    reader = csv.DictReader(file)
    students = list(reader)

# Display all records
print("All Student Records:")
for student in students:
    print(student["RollNo"], student["Name"], student["Marks"])

# Find student with highest marks
highest = max(students, key=lambda x: int(x["Marks"]))
print("\nHighest Marks:")
print(highest["Name"], "-", highest["Marks"])

# Calculate average marks
total = sum(int(student["Marks"]) for student in students)
average = total / len(students)
print("\nAverage Marks:", average)

# Students scoring more than 80
print("\nStudents scoring more than 80:")
for student in students:
    if int(student["Marks"]) > 80:
        print(student["Name"], "-", student["Marks"])

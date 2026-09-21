marks = {"Namo": 85, "Rohit": 90, "Pavan": 78}
name = input("Enter student name to update: ")
new_marks = int(input("Enter new marks: "))

if name in marks:
    marks[name] = new_marks

print(marks)
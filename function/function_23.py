def calculate_total(marks):
    return sum(marks)

def calculate_percentage(total, max_marks):
    return (total / max_marks) * 100

def calculate_grade(percentage):
    if percentage >= 90:
        return "A"
    elif percentage >= 75:
        return "B"
    elif percentage >= 60:
        return "C"
    else:
        return "D"

def class_average(all_percentages):
    return sum(all_percentages) / len(all_percentages)

def highest_scorer(students):
    highest = students[0]

    for student in students:
        if student["percentage"] > highest["percentage"]:
            highest = student

    return highest

def lowest_scorer(students):
    lowest = students[0]

    for student in students:
        if student["percentage"] < lowest["percentage"]:
            lowest = student

    return lowest

n = int(input("How many students? "))
students = []
all_percentages = []

for i in range(n):
    name = input("Enter student name: ")
    roll_no = input("Enter roll number: ")

    marks = []
    for j in range(5):
        m = int(input("Enter marks for subject " + str(j+1) + ": "))
        marks.append(m)

    total = calculate_total(marks)
    percentage = calculate_percentage(total, 500)
    grade = calculate_grade(percentage)
    all_percentages.append(percentage)

    students.append({
        "name": name,
        "roll_no": roll_no,
        "total": total,
        "percentage": percentage,
        "grade": grade
    })

for student in students:
    print(student)

print("Class Average =", class_average(all_percentages))
print("Highest Scorer:", highest_scorer(students))
print("Lowest Scorer:", lowest_scorer(students))
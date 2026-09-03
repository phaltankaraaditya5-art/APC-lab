
name = input("Enter student's name: ")
roll_no = input("Enter roll number: ")
branch = input("Enter branch: ")
semester = input("Enter semester: ")

with open("student.txt", "a") as file:
    file.write("\nName: " + name + "\n")
    file.write("Roll Number: " + roll_no + "\n")
    file.write("Branch: " + branch + "\n")
    file.write("Semester: " + semester + "\n")

print("Additional student information appended successfully.")

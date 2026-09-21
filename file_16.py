file = open("student.txt", "r")
content = file.read()
file.close()

upper_content = content.upper()

new_file = open("upper_student.txt", "w")
new_file.write(upper_content)
new_file.close()
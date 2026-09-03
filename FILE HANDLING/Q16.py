
with open("student.txt", "r") as file:
    text = file.read()

with open("uppercase.txt", "w") as file:
    file.write(text.upper())

print("Uppercase text saved in uppercase.txt")

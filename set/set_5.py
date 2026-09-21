students = {"Varad", "Pravin", "Namo", "Shiva"}
name = input("Enter name to check: ")

if name in students:
    print("Student exists")
else:
    print("Student does not exist")
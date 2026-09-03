
with open("student.txt", "r") as file:
    contents = file.read()

words = contents.split()

print("Total number of words:", len(words))

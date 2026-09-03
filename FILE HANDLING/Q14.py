
old_word = input("Enter the word to replace: ")
new_word = input("Enter the new word: ")

with open("student.txt", "r") as file:
    text = file.read()

modified_text = text.replace(old_word, new_word)

with open("student_new.txt", "w") as file:
    file.write(modified_text)

print("Word replaced successfully.")
print("Modified text saved in student_new.txt")

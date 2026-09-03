
with open("student.txt", "r") as file:
    text = file.read()

words = text.split()

if words:
    longest_word = max(words, key=len)
    print("Longest word:", longest_word)
    print("Length:", len(longest_word))
else:
    print("The file is empty.")

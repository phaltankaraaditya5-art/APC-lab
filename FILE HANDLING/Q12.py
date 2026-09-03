
with open("student.txt", "r") as file:
    text = file.read()

words = text.lower().split()

word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print("Word occurrences:")
print(word_count)

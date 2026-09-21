file = open("student.txt", "r")
content = file.read()
file.close()

words = content.split()
longest = words[0]

for word in words:
    if len(word) > len(longest):
        longest = word

print("Longest word:", longest)
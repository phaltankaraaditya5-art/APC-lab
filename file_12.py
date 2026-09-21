file = open("student.txt", "r")
content = file.read()
file.close()

words = content.split()
freq = {}

for word in words:
    if word in freq:
        freq[word] = freq[word] + 1
    else:
        freq[word] = 1

print(freq)
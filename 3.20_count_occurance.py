sentence = "python is easy and python is powerful"
word = "python"
words = sentence.split()
count = 0
for w in words:
    if w == word:
        count += 1
print(f"'{word}' occurs {count} times")
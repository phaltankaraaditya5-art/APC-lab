paragraph = "python is easy python is powerful and python is popular"
words = paragraph.split()
freq = {}
for word in words:
    freq[word] = freq.get(word, 0) + 1
print("Word frequency:", freq)
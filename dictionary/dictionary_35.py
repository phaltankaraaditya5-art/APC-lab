paragraph = input("Enter a paragraph: ")
words = paragraph.split()
freq = {}

for word in words:
    length = len(word)
    if length in freq:
        freq[length] = freq[length] + 1
    else:
        freq[length] = 1

print(freq)
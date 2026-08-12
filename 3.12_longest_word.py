sentence = "Python is a simple programming language"
words = sentence.split()
longest = words[0]
for word in words:
    if len(word) > len(longest):
        longest = word
print("Longest word:", longest)
n = int(input("How many words? "))
words = []

for i in range(n):
    w = input("Enter word: ")
    words.append(w)

sorted_words = sorted(words, key=lambda w: len(w))

print("Sorted by length:", sorted_words)
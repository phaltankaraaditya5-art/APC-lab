n = int(input("How many words? "))
words = []

for i in range(n):
    w = input("Enter word: ")
    words.append(w)

word_lengths = list(map(lambda w: (w, len(w)), words))
long_words = list(filter(lambda w: len(w) > 5, words))
sorted_words = sorted(words, key=lambda w: len(w))

print("Word lengths:", word_lengths)
print("Words with more than 5 characters:", long_words)
print("Sorted by length:", sorted_words)
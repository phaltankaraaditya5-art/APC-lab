n = int(input("How many words? "))
words = []

for i in range(n):
    w = input("Enter word: ")
    words.append(w)

long_words = list(filter(lambda w: len(w) > 5, words))

print("Words with more than 5 characters:", long_words)
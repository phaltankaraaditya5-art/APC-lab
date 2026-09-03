
with open("student.txt", "r") as file:
    text = file.read()

vowels = 0
consonants = 0

for ch in text:
    if ch.isalpha():
        if ch.lower() in "aeiou":
            vowels += 1
        else:
            consonants += 1

print("Number of vowels:", vowels)
print("Number of consonants:", consonants)

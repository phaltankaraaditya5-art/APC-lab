file = open("student.txt", "r")
content = file.read()
file.close()

vowels = 0
consonants = 0

for ch in content:
    if ch.isalpha():
        if ch.lower() in "aeiou":
            vowels = vowels + 1
        else:
            consonants = consonants + 1

print("Vowels =", vowels)
print("Consonants =", consonants)
import re
s = input("Enter a string: ")
vowels = re.findall(r"[aeiouAEIOU]", s)
print("Vowels:", vowels)
print("Total vowels =", len(vowels))
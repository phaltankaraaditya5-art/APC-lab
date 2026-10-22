import re
s = input("Enter a sentence: ")
words = re.findall(r"\b\w{5}\b", s)
print("Five-letter words:", words)
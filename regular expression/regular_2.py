import re
s = input("Enter a sentence: ")
words = re.findall(r"\b[Aa]\w*", s)
print("Words starting with A or a:", words)

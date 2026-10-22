import re
s = input("Enter a sentence: ")
words = re.findall(r"\b\w*[sS]\b", s)
print("Words ending with s:", words)
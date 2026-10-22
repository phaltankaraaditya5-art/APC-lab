import re
s = input("Enter a string: ")
digits = re.findall(r"\d", s)
print("Digits:", digits)
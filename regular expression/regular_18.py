import re
paragraph = input("Enter a paragraph: ")
pins = re.findall(r"\b[1-9]\d{5}\b", paragraph)
print("PIN codes:", pins)
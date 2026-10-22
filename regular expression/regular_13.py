import re
paragraph = input("Enter a paragraph: ")
dates = re.findall(r"\b(?:0[1-9]|[12]\d|3[01])-(?:0[1-9]|1[0-2])-\d{4}\b", paragraph)
print("Dates found:", dates)
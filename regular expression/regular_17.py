import re
s = input("Enter a sentence: ")
matches = re.findall(r"\b(\w+)\s+\1\b", s, re.IGNORECASE)
if matches:
    print("Repeated words:", matches)
else:
    print("No repeated words found")
import re
s = input("Enter a string: ")
uppercase = re.findall(r"[A-Z]", s)
print("Uppercase letters:", uppercase)
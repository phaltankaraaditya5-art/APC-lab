import re
number = input("Enter vehicle number: ")
if re.fullmatch(r"[A-Z]{2}\d{2}[A-Z]{1,2}\d{4}", number):
    print("Valid vehicle registration number")
else:
    print("Invalid vehicle registration number")
import re
email = input("Enter email address: ")
if re.fullmatch(r"[\w.+-]+@[\w-]+(\.[\w-]+)+", email):
    print("Valid email format")
else:
    print("Invalid email format")
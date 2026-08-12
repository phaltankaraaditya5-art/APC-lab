email = input("Enter email: ")

if "@" in email and "." in email:
    username, domain = email.split("@")
    if len(username) > 0 and "." in domain:
        print("Valid email")
    else:
        print("Invalid email")
else:
    print("Invalid email")
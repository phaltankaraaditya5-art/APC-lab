file = open("student.txt", "r")
content = file.read()
file.close()

alphabets = digits = spaces = special = 0

for ch in content:
    if ch.isalpha():
        alphabets = alphabets + 1
    elif ch.isdigit():
        digits = digits + 1
    elif ch == " ":
        spaces = spaces + 1
    else:
        special = special + 1

print("Alphabets =", alphabets)
print("Digits =", digits)
print("Spaces =", spaces)
print("Special characters =", special)
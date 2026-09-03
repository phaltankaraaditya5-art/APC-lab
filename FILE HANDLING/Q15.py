

with open("program.py", "r") as file:
    lines = file.readlines()

with open("program_without_comments.py", "w") as file:
    for line in lines:
        stripped_line = line.strip()

        if not stripped_line.startswith("#"):
            file.write(line)

print("Comments removed successfully.")
print("New file: program_without_comments.py")

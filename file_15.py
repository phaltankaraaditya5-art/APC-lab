source_file = open("file_15_source.py", "r")
new_file = open("file_15_cleaned.py", "w")

for line in source_file:
    if "#" in line:
        line = line.split("#")[0]
    new_file.write(line)

source_file.close()
new_file.close()
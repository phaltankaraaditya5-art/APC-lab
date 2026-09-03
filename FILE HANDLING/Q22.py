
with open("file1.txt", "r") as file1:
    content1 = file1.read()

with open("file2.txt", "r") as file2:
    content2 = file2.read()

with open("file3.txt", "w") as file3:
    file3.write(content1)
    file3.write("\n")
    file3.write(content2)

print("Contents of both files copied to file3.txt")

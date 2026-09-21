file1 = open("file1.txt", "r")
file2 = open("file2.txt", "r")

content1 = file1.read()
content2 = file2.read()

file1.close()
file2.close()

merged_file = open("merged.txt", "w")
merged_file.write(content1)
merged_file.write(content2)
merged_file.close()

print("Files merged successfully")
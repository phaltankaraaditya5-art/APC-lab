file1 = open("file1.txt", "r")
file2 = open("file2.txt", "r")

lines1 = file1.readlines()
lines2 = file2.readlines()

file1.close()
file2.close()

identical = True

for i in range(min(len(lines1), len(lines2))):
    if lines1[i] != lines2[i]:
        print("Files differ at line", i + 1)
        identical = False
        break

if identical:
    print("Files are identical")
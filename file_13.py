search_word = input("Enter word to search: ")

file = open("student.txt", "r")
lines = file.readlines()
file.close()

count = 0
line_numbers = []

for i in range(len(lines)):
    if search_word in lines[i]:
        count = count + 1
        line_numbers.append(i + 1)

print("Occurrences =", count)
print("Found on lines:", line_numbers)
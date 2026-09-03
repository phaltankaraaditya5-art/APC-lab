
search_word = input("Enter the word to search: ").lower()

count = 0
line_numbers = []

with open("student.txt", "r") as file:
    for line_number, line in enumerate(file, start=1):
        words = line.lower().split()

        if search_word in words:
            occurrences = words.count(search_word)
            count += occurrences
            line_numbers.append(line_number)

print("Number of occurrences:", count)
print("Line numbers:", line_numbers)

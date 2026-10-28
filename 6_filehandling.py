
# FILE HANDLING 

# 1. Create student.txt and write student details.

with open("student.txt", "w") as file:
    file.write("Name: Rahul\n")
    file.write("Roll Number: 101\n")
    file.write("Branch: Computer Science\n")
    file.write("Semester: 3\n")


# 2. Open a text file and display complete contents.

with open("student.txt", "r") as file:
    print(file.read())


# 3. Append additional student information.

with open("student.txt", "a") as file:
    file.write("College: ABC College\n")


# 4. Read a text file line by line.

with open("student.txt", "r") as file:
    for line in file:
        print(line.strip())


# 5. Count total number of lines.

with open("student.txt", "r") as file:
    lines = file.readlines()

print("Total Lines:", len(lines))


# 6. Count total number of words.

with open("student.txt", "r") as file:
    text = file.read()

words = text.split()
print("Total Words:", len(words))


# 7. Count total number of characters including spaces.

with open("student.txt", "r") as file:
    text = file.read()

print("Total Characters:", len(text))


# 8. Read a text file and display lines in reverse order.

with open("student.txt", "r") as file:
    lines = file.readlines()

for line in reversed(lines):
    print(line.strip())


# 9. Count vowels and consonants.

with open("student.txt", "r") as file:
    text = file.read().lower()

vowels = 0
consonants = 0

for ch in text:
    if ch.isalpha():
        if ch in "aeiou":
            vowels += 1
        else:
            consonants += 1

print("Vowels:", vowels)
print("Consonants:", consonants)


# 10. Count alphabets, digits, spaces and special characters.

with open("student.txt", "r") as file:
    text = file.read()

alphabets = digits = spaces = special = 0

for ch in text:
    if ch.isalpha():
        alphabets += 1
    elif ch.isdigit():
        digits += 1
    elif ch.isspace():
        spaces += 1
    else:
        special += 1

print("Alphabets:", alphabets)
print("Digits:", digits)
print("Spaces:", spaces)
print("Special Characters:", special)


# 11. Find the longest word.

with open("student.txt", "r") as file:
    words = file.read().split()

longest = max(words, key=len)
print("Longest Word:", longest)


# 12. Count frequency of each word using dictionary.

with open("student.txt", "r") as file:
    words = file.read().lower().split()

frequency = {}

for word in words:
    word = word.strip(".,!?")
    frequency[word] = frequency.get(word, 0) + 1

print(frequency)


# 13. Search for a word and display occurrences and line numbers.

search_word = input("Enter word to search: ").lower()
count = 0
line_numbers = []

with open("student.txt", "r") as file:
    for line_no, line in enumerate(file, 1):
        words = line.lower().split()
        occurrences = words.count(search_word)

        if occurrences > 0:
            count += occurrences
            line_numbers.append(line_no)

print("Occurrences:", count)
print("Line Numbers:", line_numbers)


# 14. Replace a word with another word.

old_word = input("Enter word to replace: ")
new_word = input("Enter new word: ")

with open("student.txt", "r") as file:
    text = file.read()

text = text.replace(old_word, new_word)

with open("student_new.txt", "w") as file:
    file.write(text)

print("Modified file created.")


# 15. Remove single-line comments from Python source file.

with open("program.py", "r") as source:
    lines = source.readlines()

with open("program_without_comments.py", "w") as target:
    for line in lines:
        stripped = line.lstrip()

        if not stripped.startswith("#"):
            target.write(line)

print("Comments removed.")


# 16. Create another file containing text in uppercase.

with open("student.txt", "r") as file:
    text = file.read()

with open("uppercase.txt", "w") as file:
    file.write(text.upper())

print("Uppercase file created.")


# 17. Student records.

with open("students.csv", "w") as file:
    file.write("RollNo,Name,Marks\n")
    file.write("101,Amit,85\n")
    file.write("102,Priya,92\n")
    file.write("103,Rahul,78\n")

students = []

with open("students.csv", "r") as file:
    next(file)

    for line in file:
        roll, name, marks = line.strip().split(",")
        students.append((int(roll), name, float(marks)))

print("All Records:")
for student in students:
    print(student)

highest = max(students, key=lambda x: x[2])
average = sum(x[2] for x in students) / len(students)

print("Highest Marks:", highest)
print("Average Marks:", average)

print("Students scoring more than 80:")
for student in students:
    if student[2] > 80:
        print(student)


# 18. Employee records.

with open("employees.csv", "w") as file:
    file.write("101,Rahul,IT,60000\n")
    file.write("102,Priya,HR,55000\n")
    file.write("103,Amit,Finance,75000\n")

employees = []

with open("employees.csv", "r") as file:
    for line in file:
        emp_id, name, department, salary = line.strip().split(",")
        employees.append(
            (int(emp_id), name, department, float(salary))
        )

def display_employees():
    for employee in employees:
        print(employee)

def highest_paid():
    return max(employees, key=lambda x: x[3])

def average_salary():
    return sum(x[3] for x in employees) / len(employees)

def above_salary(amount):
    for employee in employees:
        if employee[3] > amount:
            print(employee)

display_employees()
print("Highest Paid:", highest_paid())
print("Average Salary:", average_salary())
print("Employees above 60000:")
above_salary(60000)


# 19. Student attendance.

with open("attendance.txt", "w") as file:
    file.write("101,Rahul,80,100\n")
    file.write("102,Priya,70,100\n")
    file.write("103,Amit,90,100\n")

with open("attendance.txt", "r") as file:
    for line in file:
        roll, name, present, total = line.strip().split(",")

        percentage = (int(present) / int(total)) * 100

        print(name, "Attendance:", percentage, "%")

        if percentage < 75:
            print(name, "has attendance below 75%")


# 20. Deposits and withdrawals.

with open("transactions.txt", "w") as file:
    file.write("deposit,5000\n")
    file.write("withdrawal,1000\n")
    file.write("deposit,3000\n")
    file.write("withdrawal,500\n")

total_deposits = 0
total_withdrawals = 0
transactions = []

with open("transactions.txt", "r") as file:
    for line in file:
        transaction, amount = line.strip().split(",")
        amount = float(amount)

        transactions.append(amount)

        if transaction == "deposit":
            total_deposits += amount
        else:
            total_withdrawals += amount

final_balance = total_deposits - total_withdrawals
largest_transaction = max(transactions)

print("Total Deposits:", total_deposits)
print("Total Withdrawals:", total_withdrawals)
print("Final Balance:", final_balance)
print("Largest Transaction:", largest_transaction)


# 21. Book management.

books = {}

def add_book(book_id, title, author):
    books[book_id] = {
        "title": title,
        "author": author,
        "available": True
    }

def search_book(book_id):
    if book_id in books:
        print(books[book_id])
    else:
        print("Book not found.")

def issue_book(book_id):
    if book_id in books and books[book_id]["available"]:
        books[book_id]["available"] = False
        print("Book issued.")
    else:
        print("Book unavailable.")

def return_book(book_id):
    if book_id in books:
        books[book_id]["available"] = True
        print("Book returned.")

def available_books():
    for book_id, book in books.items():
        if book["available"]:
            print(book_id, book)

add_book(101, "Python", "John")
add_book(102, "Java", "David")

search_book(101)
issue_book(101)
return_book(101)
available_books()


# 22. Combine two text files into a third file.

with open("file1.txt", "r") as file:
    text1 = file.read()

with open("file2.txt", "r") as file:
    text2 = file.read()

with open("file3.txt", "w") as file:
    file.write(text1)
    file.write("\n")
    file.write(text2)

print("Files combined.")


# 23. Compare two text files.

with open("file1.txt", "r") as file:
    lines1 = file.readlines()

with open("file2.txt", "r") as file:
    lines2 = file.readlines()

if lines1 == lines2:
    print("Files are identical.")
else:
    print("Files are different.")

    for i in range(min(len(lines1), len(lines2))):
        if lines1[i] != lines2[i]:
            print("First difference at line:", i + 1)
            break


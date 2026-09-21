def add_book(book_id, title, author):
    file = open("books.txt", "a")
    file.write(book_id + "," + title + "," + author + ",Available\n")
    file.close()

def search_book(book_id):
    file = open("books.txt", "r")
    for line in file:
        parts = line.strip().split(",")
        if parts[0] == book_id:
            print(parts)
    file.close()

def issue_book(book_id):
    file = open("books.txt", "r")
    lines = file.readlines()
    file.close()

    new_lines = []
    for line in lines:
        parts = line.strip().split(",")
        if parts[0] == book_id:
            parts[3] = "Issued"
        new_lines.append(",".join(parts) + "\n")

    file = open("books.txt", "w")
    file.writelines(new_lines)
    file.close()

def return_book(book_id):
    file = open("books.txt", "r")
    lines = file.readlines()
    file.close()

    new_lines = []
    for line in lines:
        parts = line.strip().split(",")
        if parts[0] == book_id:
            parts[3] = "Available"
        new_lines.append(",".join(parts) + "\n")

    file = open("books.txt", "w")
    file.writelines(new_lines)
    file.close()

def display_available():
    file = open("books.txt", "r")
    for line in file:
        parts = line.strip().split(",")
        if parts[3] == "Available":
            print(parts)
    file.close()

add_book("B1", "Python Basics", "Varad")
add_book("B2", "Data Structures", "Shiva")
search_book("B1")
issue_book("B1")
display_available()
return_book("B1")
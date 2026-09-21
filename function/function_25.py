books = {}

def add_book(book_id, title):
    books[book_id] = {"title": title, "available": True}

def issue_book(book_id):
    if book_id in books and books[book_id]["available"]:
        books[book_id]["available"] = False
        print("Book issued")
    else:
        print("Book not available")

def return_book(book_id):
    if book_id in books:
        books[book_id]["available"] = True
        print("Book returned")

def search_book(book_id):
    if book_id in books:
        print(books[book_id])
    else:
        print("Book not found")

def display_available():
    for book_id, details in books.items():
        if details["available"]:
            print(book_id, "-", details["title"])

while True:
    print("\n1.Add 2.Issue 3.Return 4.Search 5.Display Available 6.Exit")
    choice = int(input("Enter choice: "))

    if choice == 1:
        book_id = input("Enter book ID: ")
        title = input("Enter book title: ")
        add_book(book_id, title)

    elif choice == 2:
        book_id = input("Enter book ID: ")
        issue_book(book_id)

    elif choice == 3:
        book_id = input("Enter book ID: ")
        return_book(book_id)

    elif choice == 4:
        book_id = input("Enter book ID: ")
        search_book(book_id)

    elif choice == 5:
        display_available()

    elif choice == 6:
        break
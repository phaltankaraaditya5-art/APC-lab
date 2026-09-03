def add_book():
    book_id = input("Enter Book ID: ")
    title = input("Enter Title: ")
    author = input("Enter Author: ")

    with open("books.txt", "a") as file:
        file.write(book_id + "," + title + "," + author + ",Available\n")

    print("Book added successfully.")


def search_book():
    book_id = input("Enter Book ID to search: ")

    with open("books.txt", "r") as file:
        for line in file:
            data = line.strip().split(",")

            if data[0] == book_id:
                print("Book ID:", data[0])
                print("Title:", data[1])
                print("Author:", data[2])
                print("Status:", data[3])
                return

    print("Book not found.")


def issue_book():
    book_id = input("Enter Book ID to issue: ")

    with open("books.txt", "r") as file:
        lines = file.readlines()

    found = False

    with open("books.txt", "w") as file:
        for line in lines:
            data = line.strip().split(",")

            if data[0] == book_id:
                found = True

                if data[3] == "Available":
                    data[3] = "Issued"
                    print("Book issued successfully.")
                else:
                    print("Book is already issued.")

            file.write(",".join(data) + "\n")

    if not found:
        print("Book not found.")


def return_book():
    book_id = input("Enter Book ID to return: ")

    with open("books.txt", "r") as file:
        lines = file.readlines()

    found = False

    with open("books.txt", "w") as file:
        for line in lines:
            data = line.strip().split(",")

            if data[0] == book_id:
                found = True
                data[3] = "Available"
                print("Book returned successfully.")

            file.write(",".join(data) + "\n")

    if not found:
        print("Book not found.")


def display_available_books():
    print("\nAvailable Books:")

    with open("books.txt", "r") as file:
        for line in file:
            data = line.strip().split(",")

            if data[3] == "Available":
                print(data[0], data[1], "-", data[2])



while True:
    print("\n--- Book Management ---")
    print("1. Add Book")
    print("2. Search Book")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Display Available Books")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_book()
    elif choice == "2":
        search_book()
    elif choice == "3":
        issue_book()
    elif choice == "4":
        return_book()
    elif choice == "5":
        display_available_books()
    elif choice == "6":
        print("Program ended.")
        break
    else:
        print("Invalid choice.")

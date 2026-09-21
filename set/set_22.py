available_books = {"Python Basics", "Data Structures", "Algorithms"}
requested_books = {"Python Basics", "Machine Learning", "Algorithms"}

available_requested = requested_books.intersection(available_books)
print("Requested books available:", available_requested)
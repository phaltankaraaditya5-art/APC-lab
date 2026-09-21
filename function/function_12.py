def is_palindrome(value):
    value = str(value)
    return value == value[::-1]

value = input("Enter a string or number: ")
print("Palindrome:", is_palindrome(value))
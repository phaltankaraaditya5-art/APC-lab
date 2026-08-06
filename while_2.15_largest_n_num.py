count = int(input("Enter how many numbers: "))
largest = int(input("Enter numbers: "))
i = 1

while i < count:
    num = int(input("Enter a number: "))
    if num > largest:
        largest = num
    i = i + 1

print("Largest =", largest)
count = int(input("Enter how many numbers: "))
smallest = int(input("Enter numbers: "))
i = 1

while i < count:
    num = int(input("Enter a number: "))
    if num < smallest:
        smallest = num
    i = i + 1

print("Smallest =", smallest)
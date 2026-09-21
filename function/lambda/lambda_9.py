n = int(input("How many numbers? "))
numbers = []

for i in range(n):
    num = int(input("Enter number: "))
    numbers.append(num)

evens = list(filter(lambda x: x % 2 == 0, numbers))

print("Even numbers:", evens)
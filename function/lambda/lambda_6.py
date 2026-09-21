n = int(input("How many numbers? "))
numbers = []

for i in range(n):
    num = int(input("Enter number: "))
    numbers.append(num)
squares = list(map(lambda x: x * x, numbers))

print("Squares:", squares)
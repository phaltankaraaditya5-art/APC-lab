n = int(input("How many numbers? "))
numbers = []

for i in range(n):
    num = int(input("Enter number: "))
    numbers.append(num)

result = list(filter(lambda x: x > 50, numbers))

print("Numbers greater than 50:", result)
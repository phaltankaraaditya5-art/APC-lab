n = int(input("How many numbers? "))
numbers = []

for i in range(n):
    num = int(input("Enter number: "))
    numbers.append(num)

positives = list(filter(lambda x: x > 0, numbers))

print("Positive numbers:", positives)
n = int(input("How many numbers? "))
numbers = []

for i in range(n):
    num = int(input("Enter number: "))
    numbers.append(num)

cubes = list(map(lambda x: x ** 3, numbers))

print("Cubes:", cubes)
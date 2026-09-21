def find_largest(numbers):
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num

    return largest

n = int(input("How many numbers? "))
numbers = []

for i in range(n):
    num = int(input("Enter number: "))
    numbers.append(num)

print("Largest =", find_largest(numbers))
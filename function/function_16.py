def second_largest(numbers):
    largest = max(numbers)
    numbers.remove(largest)
    return max(numbers)

n = int(input("How many numbers? "))
numbers = []

for i in range(n):
    num = int(input("Enter number: "))
    numbers.append(num)

print("Second largest =", second_largest(numbers))
def list_stats(numbers):
    minimum = min(numbers)
    maximum = max(numbers)
    total = sum(numbers)
    average = total / len(numbers)

    return minimum, maximum, total, average

n = int(input("How many numbers? "))
numbers = []

for i in range(n):
    num = int(input("Enter number: "))
    numbers.append(num)

minimum, maximum, total, average = list_stats(numbers)

print("Min =", minimum)
print("Max =", maximum)
print("Sum =", total)
print("Average =", average)
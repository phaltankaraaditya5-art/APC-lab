def count_occurrences(numbers, element):
    count = 0
    for num in numbers:
        if num == element:
            count = count + 1
    return count


n = int(input("How many numbers? "))
numbers = []

for i in range(n):
    num = int(input("Enter number: "))
    numbers.append(num)

element = int(input("Enter element to count: "))
print("Occurrences =", count_occurrences(numbers, element))
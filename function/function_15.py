def unique_elements(numbers):
    result = []
    for num in numbers:
        if num not in result:
            result.append(num)
    return result


n = int(input("How many numbers? "))
numbers = []
for i in range(n):
    num = int(input("Enter number: "))
    numbers.append(num)

print("Unique elements:", unique_elements(numbers))
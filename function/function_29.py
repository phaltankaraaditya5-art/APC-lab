def binary_search(numbers, target, low, high):
    if low > high:
        return -1

    mid = (low + high) // 2

    if numbers[mid] == target:
        return mid
    elif numbers[mid] < target:
        return binary_search(numbers, target, mid+1, high)
    else:
        return binary_search(numbers, target, low, mid-1)

n = int(input("How many numbers? "))
numbers = []

for i in range(n):
    num = int(input("Enter number: "))
    numbers.append(num)

numbers.sort()
target = int(input("Enter number to search: "))

result = binary_search(numbers, target, 0, len(numbers)-1)

print("Found at index:", result)
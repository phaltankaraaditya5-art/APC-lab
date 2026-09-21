numbers = [2, 7, 11, 15, 5]
target = int(input("Enter target sum: "))
seen = {}

for i in range(len(numbers)):
    remaining = target - numbers[i]
    if remaining in seen:
        print("Pair found:", remaining, "and", numbers[i])
        break
    seen[numbers[i]] = i
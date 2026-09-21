n = int(input("How many numbers in each list? "))
list1 = []
list2 = []

for i in range(n):
    num = int(input("Enter number for list1: "))
    list1.append(num)

for i in range(n):
    num = int(input("Enter number for list2: "))
    list2.append(num)
result = list(map(lambda a, b: a + b, list1, list2))

print("Sum of corresponding elements:", result)
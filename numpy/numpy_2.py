import numpy as np

list1 = []
list2 = []

print("Enter 5 elements for first array:")
for i in range(5):
    num = int(input("Enter element: "))
    list1.append(num)

print("Enter 5 elements for second array:")
for i in range(5):
    num = int(input("Enter element: "))
    list2.append(num)

arr1 = np.array(list1)
arr2 = np.array(list2)

print("Addition:", arr1 + arr2)
print("Subtraction:", arr1 - arr2)
print("Multiplication:", arr1 * arr2)
print("Division:", arr1 / arr2)
print("Modulus:", arr1 % arr2)
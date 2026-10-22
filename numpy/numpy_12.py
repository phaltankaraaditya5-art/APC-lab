import numpy as np
elements = []
for i in range(10):
    num = int(input("Enter number: "))
    elements.append(num)

arr = np.array(elements)
arr[arr > 50] = 0
print("Updated array:", arr)
import numpy as np
elements = []
for i in range(10):
    num = int(input("Enter element: "))
    elements.append(num)

arr = np.array(elements)
print("Array:", arr)
print("Size:", arr.size)
print("Data type:", arr.dtype)
print("Dimensions:", arr.ndim)
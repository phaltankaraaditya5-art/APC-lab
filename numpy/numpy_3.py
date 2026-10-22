import numpy as np
elements = []
for i in range(10):
    num = int(input("Enter number: "))
    elements.append(num)

arr = np.array(elements)
print("Maximum:", np.max(arr))
print("Minimum:", np.min(arr))
print("Sum:", np.sum(arr))
print("Average:", np.mean(arr))
import numpy as np
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])

horizontal = np.concatenate((arr1, arr2), axis=1)
vertical = np.concatenate((arr1, arr2), axis=0)
print("Horizontal concatenation:\n", horizontal)
print("Vertical concatenation:\n", vertical)
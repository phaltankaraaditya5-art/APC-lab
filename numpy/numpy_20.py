import numpy as np
arr = np.arange(1, 25).reshape(2, 3, 4)
print("Sum of all elements:", np.sum(arr))
print("Sum of each layer:", np.sum(arr, axis=0))
print("Sum along rows:", np.sum(arr, axis=2))
print("Sum along columns:", np.sum(arr, axis=1))
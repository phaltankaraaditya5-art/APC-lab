import numpy as np
arr = np.arange(1, 25).reshape(2, 3, 4)

flattened = arr.flatten()
print("Original array:\n", arr)
print("Flattened array:", flattened)
import numpy as np

a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
b = a.reshape(3, 4)
print("2D array:")
print(b)
c = a.reshape(2, 2, 3)
print("\n3D array:")
print(c)
d = a.copy()
print("\nCopied array:")
print(d)



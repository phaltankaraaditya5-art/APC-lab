import numpy as np
matrix = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
])
print("First row:", matrix[0])
print("Last column:", matrix[:, -1])
print("Diagonal elements:", np.diag(matrix))
print("Second and third rows:\n", matrix[1:3])
import numpy as np
arr = np.random.randint(1, 101, size=(3, 4, 5))
flattened = arr.flatten()

greater_than_50 = flattened[flattened > 50]
even_numbers = flattened[flattened % 2 == 0]
average = np.mean(flattened)
less_than_average = flattened[flattened < average]

print("Greater than 50:", greater_than_50)
print("Even numbers:", even_numbers)
print("Less than average:", less_than_average)
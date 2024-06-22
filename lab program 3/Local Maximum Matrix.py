import numpy as np
matrix = np.random.randint(0, 100, (5, 5))
local_max = (matrix[1:-1, 1:-1] > matrix[:-2, 1:-1]) & (matrix[1:-1, 1:-1] > matrix[2:, 1:-1]) & (matrix[1:-1, 1:-1] > matrix[1:-1, :-2]) & (matrix[1:-1, 1:-1] > matrix[1:-1, 2:])

print("Original Matrix:")
print(matrix)

print("\nLocal Maximum Matrix:")
print(local_max.astype(int))
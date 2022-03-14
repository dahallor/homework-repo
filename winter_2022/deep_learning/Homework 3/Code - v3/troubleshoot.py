import numpy as np

arr = np.array( [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[2, 11, 12], [13, 14, 15], [16, 420, 69]]] )
print(arr)
print()
print(np.mean(arr, axis = 0))
print()
print(np.mean(arr, axis = 1))
print()
print(np.mean(arr, axis = 2))
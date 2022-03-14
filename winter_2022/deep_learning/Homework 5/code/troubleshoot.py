import numpy as np

'''
arr = np.array( [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[2, 11, 12], [13, 5, 15], [16, 420, 69]]] )
print(arr)
print()
print(np.mean(arr, axis = 0))
print()
print(np.mean(arr, axis = 1))
print()
print(np.mean(arr, axis = 2))

arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]] )
print(arr2d)
print()
print(np.mean(arr2d, axis = 0))
print()
print(np.mean(arr2d, axis = 1))
print()
'''

test = ["a", "b", "c", "d", "e", "f"]
one = [1, 5, 3]
two = [2, 4, 6]

n = 2
k = len(one)
test = np.zeros((n, k, k))

test[0] = np.diag(one)
test[1] = np.diag(two)

print(test)

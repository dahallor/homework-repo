import numpy as np

X = np.array([[0, -1, 2], [2, 1, 0]])
W1 = np.array([[0, 1, 0], [1, 1, 1], [-2, 2, 1]])
W2 = np.array([[-1, 1], [0, 1], [1, 2]])
W3 = np.array([[2], [-1]])
b3 = np.array([[5]])
b2 = np.array([[1, 0]])

h1 = X.dot(W1)

act1 = h1 ** 2
h2 = act1.dot(W2)
Y2 = h2 + b2

h3 = Y2.dot(W3)
Y3 = h3 + b3
print(Y3)
import numpy as np

a = [[11,12,13],[21,22,23],[31,32,33]]

A = np.array(a)
print(A)

print(A.ndim)
print(A.shape)
print(A.size)


# Create a numpy array X
X = np.array([[1, 0], [0, 1]]) 
print(X)

# Create a numpy array Y
Y = np.array([[2, 1], [1, 2]]) 
print(Y)
print("X+Y")
Z = X+Y
print(Z)
print("X*Y")
Z = X*Y
print(Z)
print("X.dot(Y)")
Z = X.dot(Y)
print(Z)
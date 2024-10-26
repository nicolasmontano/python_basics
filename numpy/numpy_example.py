import numpy as np

# Example of broadcasting
a = np.array([1, 2, 3])
b = np.array([[1], [2], [3]])
result = a + b
print(result)

# Example of vectorized operation
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
result = a * b
print(result)

# Boolean indexing
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
mask = a > 5
# Get elements greater than 5 with dimensions
a[mask]
print(a[mask])

# Fancy indexing
indices = [0, 2]
print(a[indices, indices])


# Aggregate functions
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Sum of all elements
print(np.sum(a))

# Mean of all elements
print(np.mean(a))

# Standard deviation
print(np.std(a))

# Sum along a specific axis
print(np.sum(a, axis=0))  # Sum along columns
print(np.sum(a, axis=1))  # Sum along rows
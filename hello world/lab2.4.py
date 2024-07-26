# Import the NumPy library
import numpy as np

# Generate values from 2 to 10
# The np.arange function generates values from 2 to 10 (exclusive)
values = np.arange(2, 11)

# Reshape the array into a 3x3 matrix
matrix = values.reshape(3, 3)

# Display the 3x3 matrix
print("3x3 Matrix with values ranging from 2 to 10:")
print(matrix)

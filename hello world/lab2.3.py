# Import the NumPy library
import numpy as np

# Create arrays of 10 zeros, 10 ones, and 10 fives
zeros_array = np.zeros(10, dtype=int)  # Array of 10 zeros
ones_array = np.ones(10, dtype=int)    # Array of 10 ones
fives_array = np.full(10, 5, dtype=int)  # Array of 10 fives

# Convert arrays to strings with commas separating elements
zeros_str = np.array2string(zeros_array, separator=', ')
ones_str = np.array2string(ones_array, separator=', ')
fives_str = np.array2string(fives_array, separator=', ')

# Display each array on a separate line
print("An Array of 10 zeros:")
print(zeros_str)

print("\n An Array of 10 ones:")
print(ones_str)

print("\n An Array of 10 fives:")
print(fives_str)

# Import the NumPy library
import numpy as np

# Define the Python list
my_list = [1, 2, 3, 4, 5]

# Convert the list into a NumPy array
my_array = np.array(my_list)

# Display the NumPy array
print("NumPy Array:")
print(my_array)

# Display the first and last elements of the array
print("\nFirst element:", my_array[0])
print("Last element:", my_array[-1])

# Multiply each element by 2
modified_array = my_array * 2

# Display the modified NumPy array
print("\nModified NumPy Array (after multiplying each element by 2):")
print(modified_array)

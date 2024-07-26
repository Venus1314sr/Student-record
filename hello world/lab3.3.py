# Import the NumPy library
import numpy as np

# Define the inventory array
inventory = np.array([10, 0, 5, 0, 20, 0])

# Determine which products are out of stock
out_of_stock = inventory[inventory == 0]

# Display the out-of-stock products
print("Out of stock products:", out_of_stock)

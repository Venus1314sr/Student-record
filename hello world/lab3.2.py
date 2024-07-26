# Import the NumPy library
import numpy as np

# Define the revenue and expenses arrays
revenue = np.array([10000, 12000, 11000, 10500])
expenses = np.array([4000, 5000, 4500, 4800])

# Calculate the profit for each period (element-wise subtraction)
profit = revenue - expenses

# Display the profit
print("Profit:", profit)

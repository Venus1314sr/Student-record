# Import the NumPy library
import numpy as np

# Define the revenue for two product categories
category1_revenue = np.array([500, 600, 700, 550])
category2_revenue = np.array([450, 700, 800, 600])

# Calculate the total revenue for each period (element-wise addition)
total_revenue = category1_revenue + category2_revenue

# Display the total revenue
print("Total revenue:", total_revenue)

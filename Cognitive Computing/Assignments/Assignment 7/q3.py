import numpy as np

# Given array
a = np.array([-1.8, -1.6, -0.5, 0.5, 1.6, 1.8, 3.0])

# i. Finding floor, ceiling, truncation, and rounded values
floor_values = np.floor(a)
ceiling_values = np.ceil(a)
truncated_values = np.trunc(a)
rounded_values = np.round(a)

print("Floor Values:", floor_values)
print("Ceiling Values:", ceiling_values)
print("Truncated Values:", truncated_values)
print("Rounded Values:", rounded_values)

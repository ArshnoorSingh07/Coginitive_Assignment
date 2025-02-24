import numpy as np

# Given array
array = np.array([[1, -2, 3], [-4, 5, -6]])

# i. Element-wise absolute value
absolute_values = np.abs(array)
print("Absolute Values:\n", absolute_values)

# ii. Percentiles (25th, 50th, 75th)
overall_percentiles = np.percentile(array, [25, 50, 75])
column_percentiles = np.percentile(array, [25, 50, 75], axis=0)
row_percentiles = np.percentile(array, [25, 50, 75], axis=1)
print("Overall Percentiles:\n", overall_percentiles)
print("Column-wise Percentiles:\n", column_percentiles)
print("Row-wise Percentiles:\n", row_percentiles)

# iii. Mean, Median, and Standard Deviation
mean_value = array.mean()
median_value = np.median(array)
std_dev = array.std()
print("Mean:", mean_value)
print("Median:", median_value)
print("Standard Deviation:", std_dev)

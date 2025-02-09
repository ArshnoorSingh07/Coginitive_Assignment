# Q.2 (a)For the array: array = np.array([10, 52, 62, 16, 16, 54, 453]), find 
# i. Sorted array 
# ii. Indices of sorted array 
# iii. 4 smallest elements 
# iv. 5 largest elements 
# (b) For the array: array = np.array([1.0, 1.2, 2.2, 2.0, 3.0, 2.0]), find 
# i. Integer elements only 
# ii. Float elements only 

# a.
import numpy as np
array=np.array([10, 52, 62, 16, 16, 54, 453])
sorted_array = np.sort(array)
print("Sorted array:", sorted_array)
print("Indices of sorted array:", np.argsort(array))
print("4 smallest elements:", sorted_array[:4])
print("5 largest elements:", sorted_array[-5:])

# b.
array_b = np.array([1.0, 1.2, 2.2, 2.0, 3.0, 2.0])
int_elements = array_b[np.floor(array_b) == array_b]
float_elements = array_b[np.floor(array_b) != array_b]
print("Integer elements only:", int_elements)
print("Float elements only:", float_elements)
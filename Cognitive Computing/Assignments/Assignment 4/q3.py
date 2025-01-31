# Q.3 For the given 2-D array arr=np.array([10, 20, 30], [40, 50, 60], [70, 80, 90]), access 
# elements using row and column indices as follows: 
# a) Access 1st row, 2nd column  
# b) Access 3rd row, 1st column 

import numpy as np
arr = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
a = arr[0, 1]  
b = arr[2, 0]  
print("Element at 1st row, 2nd column:", a)
print("Element at 3rd row, 1st column:", b)

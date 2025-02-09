# Q.1 For the array gfg = np.matrix('[4, 1, 9; 12, 3, 1; 4, 5, 6]'), Find 
# i. Sum of all elements 
# ii. Sum of all elements row-wise 
# iii. Sum of all elements column-wise

import numpy as np
gfg = np.array([[4,1, 9], [12, 3, 1], [4, 5, 6]])
print("Sum of all elements:", gfg.sum())
print("Sum of all elements row-wise:", gfg.sum(axis=1))
print("Sum of all elements column-wise:", gfg.sum(axis=0))
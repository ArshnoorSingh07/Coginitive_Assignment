# Q.2 Questions on Basic NumPy Array: 
# a) Reverse the NumPy array: arr = np.array([1, 2, 3, 6, 4, 5]) 
# b) Find the most frequent value and their indice(s) in the following arrays: 
# i. x = np.array([1,2,3,4,5,1,2,1,1,1]) 
# ii. y = np.array([1, 1, 1, 2, 3, 4, 2, 4, 3, 3]) 

import numpy as np
arr=np.array([1,2,3,6,4,5])
print(f"Array:{arr}")
# a.
reversed_arr=arr[::-1]
print("After reversing:",reversed_arr)
# b.
x=np.array([1,2,3,4,5,1,2,1,1,1])
y=np.array([1, 1, 1, 2, 3, 4, 2, 4, 3, 3, ])

def most_frequent_value_and_indices(array):
    unique, counts = np.unique(array, return_counts=True)
    max_count = np.max(counts)
    most_frequent_value = unique[np.argmax(counts)]
    indices = np.where(array == most_frequent_value)[0]
    return most_frequent_value, indices

most_frequent_x, indices_x = most_frequent_value_and_indices(x)
print("Most frequent value in x:", most_frequent_x)
print("Indices of most frequent value in x:", indices_x)

most_frequent_y, indices_y = most_frequent_value_and_indices(y)
print("Most frequent value in y:", most_frequent_y)
print("Indices of most frequent value in y:", indices_y)
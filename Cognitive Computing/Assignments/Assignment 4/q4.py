# Q.4 Write program to create an 1-D NumPy array named <<Your Name>> with evenly 
# spaced 25 numbers from 10 to 100 using linspace(). Print the dimensions of the array, 
# shape, total elements, the data type of each element and total number of bytes consumed 
# by the array. Find the transpose of this array using reshape() attribute. Can we do the same 
# with T attribute? 
import numpy as np
ArshnoorSingh=np.linspace(10,100,25)
print(ArshnoorSingh)

print(f"Dimensions of array:{ArshnoorSingh.shape}")
print(f"Total elements of array:{ArshnoorSingh.size}")
print(f"Data type of each element:{ArshnoorSingh.dtype}")
print(f"Bytes consumed:{ArshnoorSingh.nbytes}")

# Finding the transpose using reshape()
transposed_array = ArshnoorSingh.reshape(25, 1)
print("\nTransposed Array using reshape():\n", transposed_array)

# Checking if we can use the T attribute
t_transpose = ArshnoorSingh.T
print("\nTransposed Array using T attribute:\n", t_transpose)

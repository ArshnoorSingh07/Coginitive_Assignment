# Q5. Create a 2-D Array of three rows and four columns, named ucs420_<your_name>> 
# with following values – 10, 20, 30, 40, 50, 60, 70, 80, 90, 15, 20, 35. Compute the mean, 
# median, max, min, unique elements. Reshape the array to four rows and three columns and 
# name it as reshaped_ ucs420_<your_name>>. Resize the array to two rows and three 
# columns and name it as resized_ ucs420_<your_name>>.
import numpy as np

ucs420_Arshnoor = np.array([[10, 20, 30, 40], [50, 60, 70, 80], [90, 15, 20, 35]])

# Computing statistics
print("\nMean:", np.mean(ucs420_Arshnoor))
print("Median:", np.median(ucs420_Arshnoor))
print("Max:", np.max(ucs420_Arshnoor))
print("Min:", np.min(ucs420_Arshnoor))
print("Unique elements:", np.unique(ucs420_Arshnoor))

# Reshaping the array to four rows and three columns
reshaped_ucs420_Arshnoor = ucs420_Arshnoor.reshape(4, 3)
print("\nReshaped Array (4x3):\n", reshaped_ucs420_Arshnoor)

# Resizing the array to two rows and three columns
resized_ucs420_Arshnoor = np.resize(ucs420_Arshnoor, (2, 3))
print("\nResized Array (2x3):\n", resized_ucs420_Arshnoor)

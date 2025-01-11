import math
import datetime
import os
# 11.1 Write a program to use the math library to calculate the square root of a given number.
def calculate_square_root(number):
    return math.sqrt(number)
number=float(input("Enter a number: "))
result=calculate_square_root(number)
print(f"The square root of {number} is {result}")


# 11.2 Write a program to use the datetime library to print the current date and time.
current_datetime = datetime.datetime.now()
print(f"The current date and time is {current_datetime}")


#  11.3 Write a program to use the 
# os library to list all files in the current directory.
def list_files_in_directory():
    return os.listdir('.')
files = list_files_in_directory()
print("Files in the current directory:")
for file in files:
    print(file)

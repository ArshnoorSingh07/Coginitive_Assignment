# 10.1 Write a program to accept two numbers as command-line arguments, add 
# them, and print the result.
import sys
if len(sys.argv)!=3:
    print("Usage: python q10.py <num1> <num2>")
    sys.exit(1)
try:
    num1=float(sys.argv[1])
    num2=float(sys.argv[2])
except ValueError:
    print("Please provide two valid numbers.")
    sys.exit(1)
result=num1+num2
print(f"The result is: {result}")


# 10.2 Write a program to accept a string as a command-line argument and print its 
# length.
if len(sys.argv)!=2:
    print("Usage: python q10.py <string>")
    sys.exit(1)
input_string=sys.argv[1]
print(f"The length of the string is: {len(input_string)}")
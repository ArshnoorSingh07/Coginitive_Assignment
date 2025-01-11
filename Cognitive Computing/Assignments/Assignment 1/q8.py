# 8.1 Write a program to handle division by zero using a 
# try-except block.
try:
    numerator=float(input("Enter the numerator: "))
    denominator=float(input("Enter the denominator: "))
    result=numerator/denominator
    print(f"The result is {result}")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Invalid input. Please enter numeric values.")
    
# 8.2 Write a program to handle invalid input (e.g., when the user enters a string 
# instead of a number).
while True:
    try:
        number=float(input("Enter a number: "))
        print(f"You entered the number:{number}")
        break
    except ValueError:
        print("Error:Invalid input.Please enter a numeric value.")
        
        
# 8.3 Write a program to demonstrate the use of 
# finally in exception handling
try:
    file=open("example.txt", "r")
    content=file.read()
    print(content)
except FileNotFoundError:
    print("Error: The file was not found.")
finally:
    if 'file' in locals() and not file.closed:
        file.close()
        print("File has been closed.")
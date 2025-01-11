# 3.1 Write a Python program to check if a number is positive, negative, or zero 
# using an if-else statement.
a=float(input('Enter a number: '))
if(a>0):
    print('Positive Number')
elif(a<0):
    print('Negative Number')
else:
    print("Zero")
    
# 3.2 Write a program to check if a given number is odd or even.
num1=int(input('Enter number: '))
if(num1%2==0):
    print('Even Number')
else:
    print('Odd Number')

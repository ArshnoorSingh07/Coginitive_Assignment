#  6.1 Write a program to count the number of vowels in a given string.
str1=input('Enter a string: ')
vowel="aeiouAEIOU"
vowel_count=0
for char in str1:
    if char in vowel:
        vowel_count=vowel_count+1
print('Vowels in given string is: ', vowel_count)

# 6.2 Write a program to reverse a string and print it.
str2=input('Enter a string: ')
reverse_string=str2[::-1]
print('Reverse string is ',reverse_string)

# 6.3 Write a program to check if a string is a palindrome.
str3=input('Enter a string: ')
if str3==str3[::-1]:
    print('Yes,PALINDROME')
else:
    print('Not a PALINDROME')
# 7.1 Write a program to create a text file, write some text into it, and then read and 
# print the content.
with open('example.txt', 'w') as file:
    file.write('Hello, this is a sample text file.')
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)
    
# 7.2 Write a program to append text to an existing file and print the updated 
with open('example.txt', 'a') as file:
    file.write('\nThis is the appended text.ARSHNOOR SINGH')
with open('example.txt', 'r') as file:
    updated_content = file.read()
    print(updated_content)
    
#  7.3 Write a program to count the number of lines in a text file.
with open('example.txt', 'r') as file:
    line_count = sum(1 for line in file)
    print(f'The number of lines in the file is: {line_count}')
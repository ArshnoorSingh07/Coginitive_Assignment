# 5.1 Create a list of 5 numbers. Write a program to find the largest and smallest 
# numbers in the list.
list1=[10,15,20,25,30]
print(list1)
maximum=max(list1)
minimum=min(list1)
print('Largest number is',maximum,'and smallest number is',minimum,'.')

# 5.2 Create a dictionary with at least 3 key-value pairs. Write a program to retrieve 
# the value of a given key
dict1={
    "Name":"Arshnoor Singh",
    "Roll no":102317161,
    "Dept":"CSE"
}
print('\n',dict1)
print(dict1["Name"])

# 5.3 Write a program to sort a list of numbers in ascending and descending order.
list2=[-2,-3,5,6,1,8]
print('\n',list2)
list2.sort()
print('Ascending Order: ',list2)
list2.sort(reverse=True)
print('Descending Order: ',list2)

#  5.4 Write a program to merge two dictionaries into one.
dic1={
    "Name":"Arsh",
    "Dept":"CSE"
}
print(dic1)
dic2={
    "Roll no":102317161,
    "Age":19
}
print('\n',dic2)
dic1.update(dic2)
print(dic1)
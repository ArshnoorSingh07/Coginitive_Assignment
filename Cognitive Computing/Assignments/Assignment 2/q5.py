# 5. Write a program to rename a key city to a location in the following dictionary.
dict={"Name":"Kelly",
      "Age":25,
      "Salary":8000,
      "City":"New York"
    }
if 'City' in dict:
    dict['Location']=dict.pop('City')
    
print(dict)
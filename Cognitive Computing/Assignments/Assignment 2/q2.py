# 2. Create a tuple of marks scored as scores = (45, 89.5, 76, 45.4, 89, 92, 58, 45) and 
# perform the following operations using tuple functions: 
# i. Identify the highest score and its index in the tuple. 
# ii. Find the lowest score and count how many times it appears. 
# iii. Reverse the tuple and return it as a list. 
# iv. Check if a specific score ‘76’ (input by the user) is present in the tuple and 
# print its first occurrence index, or a message saying it’s not present. 

scores = (45, 89.5, 76, 45.4, 89, 92, 58, 45)
print(scores)
# i.
print(f'Highest score is {max(scores)} and its index is {scores.index(max(scores))}')

# ii.
print(f'Lowest score is {min(scores)} and its count is {scores.count(min(scores))}')

# iii.
reversed_scores = list(reversed(scores))
print("Reversed Scores:", reversed_scores)

# iv.
score=int(input('Enter a score:'))
if score in scores:
    print(f'INDEX={scores.index(score)},Present in the tuple.')
else:
    print('It\'s not present')
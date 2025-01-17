# 1. Create a List L that is defined as= [10, 20, 30, 40, 50, 60, 70, 80]. 
# i. WAP to add 200 and 300 to L. 
# ii. WAP to remove 10 and 30 from L.
# iii. WAP to sort L in ascending order.  
# iv. WAP to sort L in descending order. 

L=[10,20,30,40,50,60,70,80]
print(L)

# i.
L.append(200)
L.append(300)
print(f'After adding 200 and 300 List is {L}')

# ii.
L.remove(10)
L.remove(20)
print(f'After removing 10 and 20 List is {L}')

# iii.
L.sort()
print(f'After sorting in ascending order is {L}')

# iv.
L.sort(reverse=True)
print(f'After sorting in descending order is {L}')
# 3. WAP to create a list of 100 random numbers between 100 and 900. Count and print 
# the: 
# i. All odd numbers 
# ii. All even numbers 
# iii. All prime numbers 

import random
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

numbers = [random.randint(100, 900) for _ in range(100)]
odd_numbers = [num for num in numbers if num % 2 != 0]
even_numbers = [num for num in numbers if num % 2 == 0]
prime_numbers = [num for num in numbers if is_prime(num)]

print("Total odd numbers:", len(odd_numbers))
print("Total even numbers:", len(even_numbers))
print("Total prime numbers:", len(prime_numbers))

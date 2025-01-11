import random
import string
# 9.1 Write a program to generate 5 random numbers between 1 and 100 and print 
# them.
for _ in range(5):
    print(random.randint(1, 100))
   
    
#  9.2 Write a program to generate a random number and check if it is prime
def is_prime(n):
    if n<=1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

random_number = random.randint(1, 100)
print(f"Random number: {random_number}")
if is_prime(random_number):
    print("The number is prime.")
else:
    print("The number is not prime.")
    


# 9.3 Write a program to simulate rolling a six-sided die.
def roll_die():
    return random.randint(1, 6)

print(f"Rolled a die: {roll_die()}")



#  9.4 Write a program to shuffle a list of numbers.
def shuffle_list(numbers):
    random.shuffle(numbers)
    return numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Original list: {numbers}")
shuffled_numbers = shuffle_list(numbers)
print(f"Shuffled list: {shuffled_numbers}")



# 9.5 Write a program to randomly select an item from a list.
def select_random_item(items):
    return random.choice(items)
items = ['apple', 'banana', 'cherry', 'date', 'elderberry']
selected_item = select_random_item(items)
print(f"Selected item: {selected_item}")



#  9.6 Write a program to generate a random password of given length.
def generate_password(length):
    characters=string.ascii_letters + string.digits + string.punctuation
    password=''.join(random.choice(characters) for _ in range(length))
    return password

password_length = 12
print(f"Generated password: {generate_password(password_length)}")



#  9.7 Write a program to pick a random card from a standard deck of 52 cards.
def pick_random_card():
    suits=['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks=['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    deck=[f"{rank} of {suit}" for suit in suits for rank in ranks]
    return random.choice(deck)

print(f"Picked card: {pick_random_card()}")
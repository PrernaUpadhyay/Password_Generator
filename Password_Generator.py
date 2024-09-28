
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
symbols = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']

# Convert numbers to strings for password concatenation
numbers = [str(num) for num in numbers]

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

# Randomly choose letters, symbols, and numbers
password_letters = random.choices(letters, k=nr_letters)
password_symbols = random.choices(symbols, k=nr_symbols)
password_numbers = random.choices(numbers, k=nr_numbers)

# Combine all components
password_list = password_letters + password_symbols + password_numbers

# Shuffle the combined list to randomize the order
random.shuffle(password_list)

# Join the list into a string to form the final password
password = ''.join(password_list)

print(f"Your generated password is: {password}")


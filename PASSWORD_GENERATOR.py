import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!!")

nr_letters = int(input("How many letters would you like in your password? "))
nr_symbols = int(input(f"How many symbols would you like? "))
nr_numbers = int(input(f"How many numbers would you like? "))

print("")
# Level 1 - Password generation based on user input in sequential order
print("PASSWORD GENERATOR - SEQUENTIAL ORDER")
password = ""
for char in range(1, nr_letters + 1):
    password += random.choice(letters)

for char in range(1, nr_symbols + 1):
    password += random.choice(symbols)

for char in range(1, nr_numbers + 1):
    password += random.choice(numbers)

print(f"Your password is: {password}")

# print("")
# # Level 2 - Password generation based on user input in random order
# print("PASSWORD GENERATOR - RANDOM ORDER")
# password_list = []
# for char in range(1, nr_letters + 1):
#     password_list += random.choice(letters)
#
# for char in range(1, nr_symbols + 1):
#     password_list += random.choice(numbers)
#
# for char in range(1, nr_numbers + 1):
#     password_list += random.choice(symbols)
#
# # Shuffle - Function to shuffle elements within a list
# random.shuffle(password_list)
# # print(password_list)
#
# password = ""
# for char in password_list:
#     password += char
#
# print(f"Your password is: {password}")


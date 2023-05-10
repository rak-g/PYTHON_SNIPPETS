# Display input and output
print("INPUT AND OUTPUT")
print("Hello python")
print("Hello python\nHello python")
print("Hello" + " python")
print("Hello" + " " + "python")
# F-String
value = "PYTHON"
print(f"Hello {value}")
# input from command prompt
print(input("What is your name? "))
# Concatenation along with input from command prompt
print("Hello" + " " + input("What is your name? "))
# Print length of character for entered name
name = input("What is your name? ")
print("Characters in a string", len(name))

print("")
print("********************************************")
print("")

# Data types
print("DATA TYPES")
# Print integer
print(12 + 12)
# Print float
print(12.34)
# Print boolean
print(True)

print("")

# Print respective character within string - Subscripting(Disecting of string)
print("123Hello"[4])
# Print string concatenation value
print(str(7) + str(4))

print("")
print("********************************************")
print("")

# Type conversions
print("TYPE CONVERSIONS")
number = float(10.5)
print(type(number))

print("")

# Explicit conversions
new_number = str(number)
print(new_number)

print("")

# Implicit conversions
print(70 + float(10.5))

print("")
print("********************************************")
print("")

# Mathematical operations
print("COMPUTATIONS")
print(8 + 3)
print(8 - 3)
print(8 * 3)
print(8 / 3)
# Round to certain decimal places/whole number
print(round(8 / 3, 2))
print(round(8 / 3))
# Extracting 2 decimal places having 0 in its decimal
float_number = 33.60
test = "{:.2f}".format(float_number)
print(float_number)
# Extract only the whole number part in floating number
print(8 // 3)
# Exponential case
print(8 ** 3)

print("")
print("********************************************")
print("")

# Conditional operators
print("IF/ELSE CLAUSE")
height = int(input("Please enter your height in cm "))
if height > 120:
    print("You can ride roller coaster")
else:
    print("You can't ride roller coaster")

print("")
print("********************************************")
print("")

print("NESTED IF/ELSE CLAUSE")
height = int(input("Please enter your height in cm "))
age = int(input("Please enter your age "))
if height > 120:
    if age > 18:
        print("Please pay $12. ")
    else:
        print("Please pay $7. ")
else:
    print("You can't ride roller coaster")

print("")
print("********************************************")
print("")

print("ELIF CLAUSE")
height = int(input("Please enter your height in cm "))
age = int(input("Please enter your age "))
if height > 120:
    if age < 12:
        print("Please pay $5. ")
    elif age <= 18:
        print("Please pay $7. ")
    else:
        print("Please pay $12. ")
else:
    print("You can't ride roller coaster")

print("")
print("********************************************")
print("")

print("MULTIPLE ELIF CLAUSE")
height = int(input("Please enter your height in cm "))
age = int(input("Please enter your age "))
bill = 0
if height > 120:
    print("You can ride roller coaster")
    if age < 12:
        print("Child tickets. Please pay $5. ")
        bill = 5
    elif age <= 18:
        print("Youth tickets. Please pay $7. ")
        bill = 7
    elif 45 <= age <= 55:
        print("Everything is going to be good.Have a safe ride")
        bill = 12
    else:
        print("Adult tickets. Please pay $12. ")
        bill = 12
    photo = input("Do you want picture:Type Y or N. ")
    if photo == "Y":
        bill += 3
    print(f"Your final bill is ${bill}")
else:
    print("You can't ride roller coaster")

print("")
print("********************************************")
print("")

# Randomization-The process of generating random numbers inclusive of the range specified
print("RANDOMIZATION")

import random

random_integer = random.randint(0, 1)
print(f"Integer(Specific range): {random_integer}")

random_float = round(random.random(), 2)
random_float_number = round(random.uniform(1.5, 2.5), 2)
print(f"Float(0.0,1.0): {random_float}")
print(f"Float(Specific range): {random_float_number}")

print("")
print("********************************************")
print("")

# For Loop
print("FOR LOOP")
# Lists - Sequence of similar/dissimilar datatypes
web_series = ["Wednesday", "You", "Ozark"]
for index in web_series:
    print("English Series - " + index)
# Range Function-range(a[inclusive],b[exclusive])
print("")

print("SPLIT USAGE")
fruit = "apple#banana#cherry#orange"

# Replace # with comma
print(fruit.split("#", ))
# Extract first two elements in a string(0,1) & the rest clubbed in final string(2)
print(fruit.split("#", 2))

print("")

print("RANGE-IN-SUM USAGE")
for number in range(1, 11, 2):
    print(number)

print("")

number_list = [1, 2, 3]
if 2 in number_list:
    print("True")
print("Sum: ", sum(number_list))

print("")
print("********************************************")
print("")

# Scope
# Global scope - Visibility to entire file
enemies = 1

print("SCOPE VARIABLES")


def increase_enemies():
    # Local scope - Visibility within scope where it is declared
    enemies = 2
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")

print("")
print("********************************************")
print("")

# Math-magic
# n=100
# 100+99+98...3+2+1
# Sum 100+1, 99+2, 98+3....=101
# 101*50
# Display total sum of n natural numbers
print("SUM OF 100 NATURAL NUMBERS")
total = 0
for number in range(1, 101):
    total += number
print(total)

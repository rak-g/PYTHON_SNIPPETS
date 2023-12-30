# Function - Bundling a complex logic inside an indented block and performing operations retative times

# Simple function
print("SIMPLE FUNCTION")


# Function decalaration
def greet():
    print("Hi")
    print("Good evening")
    print("Have a nice day")

# Function definition
greet()

print("")
print("********************************************")
print("********************************************")
print("")


# Function with return type
def addition(number1, number2):
    result = number1 + number2
    return result


print("Sum = ", addition(10, 11))

print("")
print("********************************************")
print("********************************************")
print("")

# Parameterized function
print("PARAMETERIZED FUNCTION")


def greet_with_name(name):
    print(f"Hi {name}")
    print("Good evening")
    print("Have a nice day")


# Parameter - Name/Identity associated with the data used inside function(name)
# Argument - Actual piece of data passed to a function(Dhvani)
# Parameter = Argument
greet_with_name("Dhvani")

print("")
print("********************************************")
print("********************************************")
print("")

# Multi-Parameterized function
print("MULTI-PARAMETERIZED FUNCTION")


def greet_with_name(name, location):
    print(f"Hi {name}")
    print("Good evening")
    print("Have a nice day")
    print(f"Hope weather is moderate in {location}")


# Parameter - Name/Identity associated with the data used inside function(name)
# Argument - Actual piece of data passed to a function(Dhvani)
# Parameter = Argument

# Positional arguments
greet_with_name("Dhvani", "Bengaluru")
# Key arguments
greet_with_name(location="London", name="Christina")

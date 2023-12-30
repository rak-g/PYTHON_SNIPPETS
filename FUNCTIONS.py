# Simple function - Declaration and Defination
print("SIMPLE FUNCTION")


def greet():
    print("Hi")
    print("Good evening")
    print("Have a nice day")


greet()

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

print("")
print("********************************************")
print("********************************************")
print("")

# Functions with output
print("OUTPUT FUNCTIONS")


def format_name(first_name, last_name):
    # DocString - Document module, class, function to enhance readability
    """Formatted first and last name"""
    return f"Full name : {first_name.title()} {last_name.title()}"


print(format_name("raksha", "g"))

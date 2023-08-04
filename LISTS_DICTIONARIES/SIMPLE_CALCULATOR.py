# SIMPLE CALCULATOR - ADD, SUBTRACT, MULTIPLY, DIVIDE
# Scenario 1 - Continue with calculation whenever 'y' is encountered
# Scenario 2 - Continue with new calculation whenever 'n' is encountered
# Scenario 3 - Exit calculation whenever 'e' is encountered

print("SIMPLE CALCULATOR")


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    if n2 != 0:
        return n1 / n2
    else:
        return "Infinity"


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():
    logo = """
     _____________________
    |  _________________  |
    | | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
    | |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
    |  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
    | | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
    | |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
    | | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
    | |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
    | | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
    | |___|___|___| |___| | | |              | || |              | || |              | || |              | |
    | | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
    | |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
    |_____________________|
    """
    print(logo)
    num1 = float(input("What's the first number? "))
    for symbol in operations:
        print(symbol)

    should_continue = True
    while should_continue:
        operation_symbol = input("Pick a operation to be performed ")
        num2 = float(input("What's the second number? "))

        calculation_operation = operations[operation_symbol]
        result = calculation_operation(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {result}")
        continue_calculate = input(
            f"Type 'y' to continue calculating with {result}, type 'n' to start with new calculation, type e to exit ")

        if continue_calculate == 'y':
            num1 = result
        elif continue_calculate == 'n':
            should_continue = False
            calculator()
        elif continue_calculate == 'e':
            exit()


# Function call
calculator()

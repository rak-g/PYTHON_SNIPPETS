# Divisible by 3 - Fizz
# Divisible by 5 - Buzz
# Divisible by both 3 & 5 - FizzBuzz

print("Numbers (1-100)")
print("")

for number in range(1, 101, 1):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)

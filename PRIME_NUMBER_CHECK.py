
def prime_checker(number):
    # define a flag variable
    is_Prime = True

    if number == 1:
        print("It's not a prime number")
    elif number > 1:
        # check for factors
        for i in range(2, number):
            if (number % i) == 0:
                # if factor is found, set flag to True
                is_Prime = False
                # break out of loop
                break

    # check if flag is True
    if is_Prime:
        print("It's a prime number")
    else:
        print("It's not a prime number")
   

n = int(input("Check this number: "))
prime_checker(number=n)

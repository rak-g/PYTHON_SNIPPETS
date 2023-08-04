# Identify whether a year is a leap year/not
# Leap year cases
# Scenario 1-Divisible(4) and Divisible(100) and Divisible(400)
# Scenario 2-Divisible(4) and Not Divisible(100)
print("LEAP YEAR DEPICTION")

year = int(input("Which year do you want to check? "))
if year % 4 == 0:
    if year % 4 == 100:
        if year % 4 == 400:
            print("Leap year.")
        else:
            print("Not leap year.")
    else:
        print("Leap year.")
else:
    print("Not leap year.")

print("")
print("****************************************************************************************")
print("****************************************************************************************")
print("")

# Identify number of days based on month and year
print("PREDICTION OF NUMBER OF DAYS IN A MONTH")


def is_leap(year_input):
    if year_input % 4 == 0:
        if year_input % 4 == 100:
            if year_input % 4 == 400:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_in_month(year_input, month_input):
    if month_input < 1 or month_input > 12:
        return "Invalid month"
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(year_input) and month_input == 2:
        return 29
    return month_days[month_input - 1]


year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
total_days = days_in_month(year, month)
print(total_days)

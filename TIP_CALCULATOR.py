# BILL WITH TIP CALCULATION
# Collect bill, tip(10,12,15), people
# bill_with_tip = (tip/100 * bill) + bill

print("Welcome to Tip Calculator!!")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12 or 15 "))
people = int(input("How many people to split the bill? "))
bill_with_tip = (tip/100 * bill) + bill
final_amount = bill_with_tip/people
# Format float number to 2 decimal places retaining 0 if no number is present 
final_amount = "{:.2f}".format(round(final_amount,2))
print(f"Each person should pay ${final_amount}")


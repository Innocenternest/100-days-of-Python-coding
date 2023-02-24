print("Welcome to tip calculator")

#Take input of the bill, tip and how many people sharing the bill

bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill?"))

tip_in_percentage = tip / 100
total_tip_amount = bill * tip_in_percentage
total_bill = bill + total_tip_amount
total_bill_per_person = total_bill / people
final_amount = round(total_bill_per_person, 2)

print(final_amount)

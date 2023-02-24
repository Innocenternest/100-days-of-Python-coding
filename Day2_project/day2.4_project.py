#If you were to live 90 years, calculator how many days, weeks and month left using f-string.

age = int(input("How old are you? "))

years = 90 - age
weeks = round(years * 54)
months = round(years * 12)
days = round(years * 365)

print(f"You have {days} days, {weeks} weeks, and {months} months left")

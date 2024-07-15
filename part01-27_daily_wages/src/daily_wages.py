# Write your solution here
wage = float(input("Hourly wage: "))
hours = int(input("Hours worked: "))
day = input("Day of the week: ")

dailyWage = wage * hours

if day == "Sunday":
    dailyWage *= 2
    
print(f"Daily wages: {dailyWage} euros")
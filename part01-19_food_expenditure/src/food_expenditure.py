# Write your solution here
times = int(input("How many times a week do you eat at the student cafeteria? "))
price = float(input("The price of a typical student lunch? "))
money = float(input("How much money do you spend on groceries in a week? "))
print()
print("Average food expenditure:")
print(f"Daily: {(times * price + money) / 7} euros")
print(f"Weekly: {times * price + money} euros")
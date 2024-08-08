# Write your solution here
from datetime import datetime

eve = datetime(1999, 12, 31)
day, month, year = int(input("Day: ")), int(input("Month: ")), int(input("Year: "))
birthdate = datetime(year, month, day)
age = eve - birthdate

if birthdate > eve:
    print("You weren't born yet on the eve of the new millennium.")
else:
    print(f"You were {age.days} days old on the eve of the new millennium.")

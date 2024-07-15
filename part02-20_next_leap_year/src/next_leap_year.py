# Write your solution here
year = int(input("Year:"))
leapYear = 0
nextYear = year + 1

while True:
    if nextYear % 4 == 0:
        if nextYear % 100 == 0 and nextYear % 400 == 0:
            leapYear = nextYear
            break
        if nextYear % 100 != 0 and nextYear % 400 != 0:
            leapYear = nextYear
            break
    nextYear += 1
                
print(f"The next leap year after {year} is {leapYear}")
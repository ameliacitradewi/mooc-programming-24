# Write your solution here
limit = int(input("Limit:"))
total = 1
number = 1
result = f"{number}"

while limit > total:
    number += 1
    total += number
    result += f" + {number}"
    

print("The consecutive sum:", result, "=", total)
# Write your solution here
print("Person 1:")
name1 = input("Name:")
age1 = int(input("Age:"))

print("Person 2:")
name2 = input("Name:")
age2 = int(input("Age:"))

if age1 > age2:
    print("The elder is", name1)
elif age1 < age2:
    print("The elder is", name2)
else:
    print(name1, name2, "are the same age")
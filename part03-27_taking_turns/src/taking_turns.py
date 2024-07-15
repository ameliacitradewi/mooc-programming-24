# Write your solution here
number = int(input("Please type in a number:"))

i = 1

while i <= number:
    print(i)
    if i != number:
        print(number)
    i += 1
    number -= 1
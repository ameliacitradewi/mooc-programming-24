# Write your solution here
user_input = int(input("Please type in a positive integer: "))

for number in range(-user_input, user_input + 1):
    if number == 0:
        continue
    print(number)
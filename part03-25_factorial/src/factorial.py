# Write your solution here
while True:
    user_input = int(input("Please type in a number:"))
    number = user_input
    result = 1
    if number == 0 or number < 0:
        break
    while number > 0:
        result *= number
        number -= 1
    print(f"The factorial of the number {user_input} is {result}")
       
print("Thanks and bye!")
# Write your solution here
attempt = 0
pin = 4321

while True:
    userInput = int(input("PIN:"))
    attempt += 1

    if userInput == pin:
        break
    if userInput != pin:
        print("Wrong")

if attempt == 1:
    print("Correct! It only took you one single attempt!")
else:
    print(f"Correct! It took you {attempt} attempts")
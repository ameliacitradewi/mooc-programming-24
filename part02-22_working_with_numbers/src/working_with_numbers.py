# Write your solution here
typed = 0
total = 0
negative = 0
positive = 0

print("Please type in integer numbers. Type in 0 to finish.")

while True:
    numbers = int(input("Number:"))
    typed += 1
    total += numbers
    if numbers < 0:
        negative += 1
    else:
        positive += 1

    if numbers == 0:
        typed -= 1
        positive -= 1
        break

print("Numbers typed in", typed)
print("The sum of the numbers is", total)
print("The mean of the numbers is", total/typed)
print("Positive numbers", positive)
print("Negative numbers", negative)
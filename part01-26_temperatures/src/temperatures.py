# Write your solution here
temperature = int(input("Please type in a temperature (F): "))
celcius = 5 / 9 * (temperature - 32)

print(f"{temperature} degrees Fahrenheit equals {celcius} degrees Celsius")

if celcius < 0:
    print("Brr! It's cold in here!")
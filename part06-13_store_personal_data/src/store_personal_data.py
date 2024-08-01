# Write your solution here
def store_personal_data(person: tuple):
    with open("people.csv", 'w') as file:
        name, age, height = person[0], int(person[1]), float(person[2])
        print(name, age, height)
        line = f"{name};{age};{height}"
        file.write(line + "\n")
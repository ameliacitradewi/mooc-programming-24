# Write your solution here
the_list = []

while True:
    user_input = int(input("New Item: "))
    if user_input != 0:        
        the_list.append(user_input)
        print(f"The list now: {the_list}")
        print(f"The list in order: {sorted(the_list)}")
    else:
        print("Bye!")
        break
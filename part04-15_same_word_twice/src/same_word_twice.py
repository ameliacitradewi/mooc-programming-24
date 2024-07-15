# Write your solution here
the_list = []

while True:
    user_input = input("Word: ")
    if user_input not in the_list:
        the_list.append(user_input)
    else:
        print(f"You typed in {len(the_list)} different words")
        break
# Write your solution here
the_list = []
number = 1

while True:
    print(f"The list is now {the_list}")
    user_input = input("a(d)d, (r)emove or e(x)it: ")
    if user_input != "x":
        if user_input == "d":
            the_list.append(number)
            number += 1
        elif user_input == "r":
            the_list.pop()
            number -= 1
    else:
        print("Bye!")
        break
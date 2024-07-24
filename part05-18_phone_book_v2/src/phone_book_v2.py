# Write your solution here
phone = {}

while True:
    command = (input("command (1 search, 2 add, 3 quit): "))
    if command == "1":
        name = input("name: ")
        if name in phone:
            for number in phone[name]:
                print(number)
        else:
            print("no number")
    elif command == "2":
        name = input("name: ")
        numbers = (input("number: "))
        if name in phone:
            phone[name].append(numbers)
        else:
            phone[name] = [numbers]
        print("ok!")
    else:
        print("quitting...")
        break
# Write your solution here
phone = {}

while True:
    command = (input("command (1 search, 2 add, 3 quit): "))
    if command == "1":
        name = input("name: ")
        if name in phone:
            print(phone[name])
        else:
            print("no number")
    elif command == "2":
        name = input("name: ")
        numbers = (input("number: "))
        phone[name] = numbers
        print("ok!")
    else:
        print("quitting...")
        break
# Write your solution here
file_name = "diary.txt"

def add_entries():
    diary_entry = input("Diary entry: ")
    with open(file_name, 'a') as file:
        file.write(diary_entry + "\n")
    print("Diary saved")
    
def read_entries():
    with open(file_name, 'r') as file:
        print("Entries:")
        for lines in file:
            lines = lines.replace("\n", "")
            print(lines)

while True:
    print("1 - add an entry, 2 - read entries, 0 - quit")
    user_input = input("Function: ")
    if user_input == "1":
        add_entries()
    elif user_input == "2":
        read_entries()
    elif user_input == "0":
        print("Bye now!")
        break
    else:
        print("Input 1, 2, or 0!")



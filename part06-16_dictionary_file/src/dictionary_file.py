# Write your solution here
# Read the existing dictionary entries from the file
dictionary = {}

try:
    with open("dictionary.txt", "r") as file:
        for line in file:
            finnish, english = line.strip().split(" - ")
            dictionary[finnish] = english
except FileNotFoundError:
    # If the file does not exist, start with an empty dictionary
    pass

while True:
    print("1 - Add word, 2 - Search, 3 - Quit")
    choice = input("Function: ")

    if choice == "1":
        finnish = input("The word in Finnish: ")
        english = input("The word in English: ")
        dictionary[finnish] = english
        with open("dictionary.txt", "a") as file:
            file.write(f"{finnish} - {english}\n")
        print("Dictionary entry added")
    elif choice == "2":
        search_term = input("Search term: ")
        found = False
        for finnish, english in dictionary.items():
            if search_term in finnish or search_term in english:
                print(f"{finnish} - {english}")
                found = True
    elif choice == "3":
        print("Bye!")
        break
       
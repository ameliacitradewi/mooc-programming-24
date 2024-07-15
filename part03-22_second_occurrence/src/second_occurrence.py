# Write your solution here
word = input("Please type in a string:")
substring = input("Please type in a substring:")

first_index = word.find(substring)

if substring not in word:
    print("The substring does not occur twice in the string.")
    
if first_index != -1:
    second_index = word.find(substring, first_index + len(substring))

    if second_index == -1:
        print("The substring does not occur twice in the string.")
    else:
        print(f"The second occurrence of the substring is at index {second_index}.")
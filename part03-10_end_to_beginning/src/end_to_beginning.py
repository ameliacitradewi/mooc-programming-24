# Write your solution here
string = input("Please type in a string:")
length = len(string)
index = 0

while index < length:
    length -= 1
    print(string[length])
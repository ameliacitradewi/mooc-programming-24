# Write your solution here
word = input("Please type in a string:")
index = -1
counter = 0

while counter < len(word) :
    print(word[index:])
    index -= 1
    counter += 1

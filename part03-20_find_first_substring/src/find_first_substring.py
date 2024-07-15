# Write your solution here
word = input("Please type in a word:")
characters = input("Please type in a character:")
index = word.find(characters)

if index >= 0 and index <= len(word) - 3:
    result = word[index:(index + 3)]
    print(result)
else:
    pass
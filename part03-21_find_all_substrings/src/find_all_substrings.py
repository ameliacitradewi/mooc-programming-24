# Write your solution here
word = input("Please type in a word:")
character = input("Please type in character:")
index = word.find(character)

if index != -1:
    while index != -1:
        if (index + 3 <= len(word)):
            next_word = word[index:index + 3]
            print(next_word)
            index = word.find(character, index + 1)
        else:
            break
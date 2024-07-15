# Write your solution here
lastWord = ""
sentence = ""

while True:
    word = input("Please type in a word:")
    if word == 'end' or word == lastWord:
        break
    sentence += word + ' '
    lastWord = word

print(sentence)
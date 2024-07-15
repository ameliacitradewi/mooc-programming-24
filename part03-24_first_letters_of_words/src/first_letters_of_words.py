# Write your solution here
sentence = input()
words = sentence.split(" ")
word = 0

while word < len(words):
    print(words[word][:1])
    word += 1
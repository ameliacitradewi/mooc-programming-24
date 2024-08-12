# write your solution here
import difflib

text = input("write text: ")
wordlist = []  # The complete word from wordlist.txt

check = text.split()
checked_text = []  # save the checked word as list
misspelled = []  # save the misspelled word for suggestions

with open("wordlist.txt") as file:
    for line in file:
        line = line.replace("\n", "")
        word = line.strip().lower()
        wordlist.append(word)

for char in check:
    if char.lower() not in wordlist:
        misspelled.append(char.lower())
        checked_text.append(f"*{char}*")
    else:
        checked_text.append(char)

print(" ".join(checked_text))
print("suggestions:")

for words in misspelled:
    suggestions = difflib.get_close_matches(words, wordlist)
    print(f"{words}: {', '.join(suggestions)}")




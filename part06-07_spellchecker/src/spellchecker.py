# write your solution here
text = input()
wordlist = []

check = text.split()
checked_text = []

with open("wordlist.txt") as file:
    for line in file:
        line = line.replace("\n", "")
        word = line.strip().lower()
        wordlist.append(word)

for char in check:
    if char.lower() not in wordlist:
        checked_text.append(f"*{char}*")
    else:
        checked_text.append(char)

print(" ".join(checked_text))
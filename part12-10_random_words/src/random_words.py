# Write your solution here:
# traditional solution
def word_generator(characters: str, length: int, amount: int):
    substring = (characters[i : i + length] for i in range(amount))
    return substring

# another way using library
import random

def word_generator(characters: str, length: int, amount: int):
    return (''.join(random.choice(characters) for _ in range(length)) for _ in range(amount))

# Example Usage
wordgen = word_generator("abcdefg", 3, 5)
for word in wordgen:
    print(word)
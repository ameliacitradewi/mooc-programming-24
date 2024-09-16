# Write your solution here:
import random

def word_generator(characters: str, length: int, amount: int):
    return (''.join(random.choice(characters) for _ in range(length)) for _ in range(amount))

# Example Usage
wordgen = word_generator("abcdefg", 3, 5)
for word in wordgen:
    print(word)
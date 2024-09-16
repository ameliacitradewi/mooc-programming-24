# Write your solution here:
import random

def word_generator(characters: str, length: int, amount: int):
    return (''.join(random.choice(characters) for _ in range(length)) for _ in range(amount))
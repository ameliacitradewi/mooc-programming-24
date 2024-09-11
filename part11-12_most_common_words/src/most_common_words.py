# WRITE YOUR SOLUTION HERE:
import string
from collections import Counter

def most_common_words(filename: str, lower_limit: int):
    with open(filename, 'r') as file:
        text = file.read()

    text = text.translate(str.maketrans('','', string.punctuation))
    words_counts = Counter(text.split())

    return {word: count for word, count in words_counts.items() if count >= lower_limit}

# Example Usage
print(most_common_words("comprehensions.txt", 3))
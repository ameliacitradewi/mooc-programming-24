# Write your solution here
import random

def words(n: int, beginning: str) -> list:
    with open('words.txt', 'r') as file:
        all_words = file.read().splitlines()
    
    filtered_words = [word for word in all_words if word.startswith(beginning)]
    
    selected_words = random.sample(filtered_words, n)
    
    return selected_words

# Example usage
# try:
#     word_list = words(3, "ca")
#     for word in word_list:
#         print(word)
# except ValueError as e:
#     print(e)
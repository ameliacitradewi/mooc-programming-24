# Write your solution here
def no_vowels(my_string):
    return (my_string.translate(
        {ord(i): None for i in 'aiueo'}
        ))
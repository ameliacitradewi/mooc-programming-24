# WRITE YOUR SOLUTION HERE:
def lengths(strings: list):
    return {string : len(string) for string in strings}


# Example Usage
word_list = ["once", "upon" , "a", "time", "in"]

word_lengths = lengths(word_list)
print(word_lengths)
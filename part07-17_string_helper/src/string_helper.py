# Write your solution here
def change_case(orig_string: str):
    return orig_string.swapcase()

def split_in_half(orig_string: str) -> tuple:
    mid = len(orig_string) // 2
    return (orig_string[:mid], orig_string[mid:])

def remove_special_characters(orig_string: str):
    allowed_characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 "
    result = []
    for char in orig_string:
        if char in allowed_characters:
            result.append(char)
    return ''.join(result)
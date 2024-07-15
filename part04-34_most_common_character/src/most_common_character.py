# Write your solution here
def most_common_character(text):
    most_common_char = ""
    max_count = 0

    for i in text:
        count = text.count(i)

        if count > max_count:
            max_count = count
            most_common_char = i
    return most_common_char
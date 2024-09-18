# Write your solution here
import re

def is_dotw(my_string: str):
    regex = "^(Mon|Tue|Wed|Thu|Fri|Sat|Sun)"
    return bool(re.search(regex, my_string))

def all_vowels(my_string: str):
    regex = "^[aiueo]*$"
    return bool(re.search(regex, my_string))

def time_of_day(my_string: str):
    regex = "^([01]\d|2[0-3]):[0-5]\d:[0-5]\d$"
    return bool(re.findall(regex, my_string))

# Test Case
print(is_dotw("Mon"))  # True
print(is_dotw("Fri"))  # True
print(is_dotw("Tui"))  # False
print(all_vowels("eioueioieoieou"))  # True
print(all_vowels("autoooo"))  # False
print(time_of_day("12:43:01"))  # True
print(time_of_day("AB:01:CD"))  # False
print(time_of_day("17:59:59"))  # True
print(time_of_day("33:66:77"))  # False
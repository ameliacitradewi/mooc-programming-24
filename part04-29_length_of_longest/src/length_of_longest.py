# Write your solution here
def length_of_longest(my_list):
    length = len(max(my_list, key=len))
    return length
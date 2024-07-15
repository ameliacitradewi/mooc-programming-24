# Write your solution here
def everything_reversed(my_list):
    i = len(my_list) - 1
    reversed_list = [] # store reversed index from original list
    last_reversed = [] # store reversed string from reversed_list
    while i >= 0:
        reversed_list.append(my_list[i])
        i -= 1
    for j in reversed_list:
        last_reversed.append(j[::-1])
    return last_reversed

# another way
def everything_reversed(strings):
    # Reverse each string in the list
    reversed_strings = [s[::-1] for s in strings]
    # Reverse the order of the list
    reversed_list = reversed_strings[::-1]
    return reversed_list

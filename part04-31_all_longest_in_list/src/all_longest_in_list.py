# Write your solution here
def all_the_longest(my_list):
    longest = len(max(my_list, key=len))
    longest_list = []
    for i in my_list:
        if len(i) == longest:
            longest_list.append(i)
    return longest_list
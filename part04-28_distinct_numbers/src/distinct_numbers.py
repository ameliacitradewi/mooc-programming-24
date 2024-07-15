# Write your solution here
def distinct_numbers(my_list):
    # Create an empty list to store distinct numbers
    distinct_list = []
    
    # Iterate through each number in the input list
    for number in my_list:
        # If the number is not already in the distinct list, add it
        if number not in distinct_list:
            distinct_list.append(number)
    
    # Sort the distinct list in ascending order
    distinct_list.sort()
    
    return distinct_list

# Write your solution here
def longest_series_of_neighbours(lst):
    longest_length = 1
    current_length = 1

    for i in range(1, len(lst)):
        if abs(lst[i] - lst[i - 1]) == 1:
            current_length += 1
        else:
            if current_length > longest_length:
                longest_length = current_length
            current_length = 1

    if current_length > longest_length:
        longest_length = current_length

    return longest_length

    


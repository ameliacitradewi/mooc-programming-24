# Write your solution here
def count_matching_elements(my_matrix: list, element: int) -> int:
    counter = 0
    for i in range(len(my_matrix)):
        for j in range(len(my_matrix[i])):
            if my_matrix[i][j] == element:
                counter += 1
    return counter

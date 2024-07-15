# Write your solution here
def block_correct(sudoku: list, row_no: int, column_no: int):
    # Initialize a list to track seen numbers
    seen = []
    
    # Loop through the 3x3 block
    for r in range(row_no, row_no + 3):
        for c in range(column_no, column_no + 3):
            num = sudoku[r][c]
            # If the number is not zero and has already been seen, return False
            if num != 0:
                if num in seen:
                    return False
                seen.append(num)
    # If no duplicates are found, return True
    return True
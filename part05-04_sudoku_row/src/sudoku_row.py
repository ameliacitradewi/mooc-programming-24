# Write your solution here
def row_correct(sudoku: list, row_no: int) -> bool:
    row = sudoku[row_no]
    seen = []
    for num in row:
        if num != 0:  # Skip empty cells
            if num in seen:
                return False
            seen.append(num)
    return True
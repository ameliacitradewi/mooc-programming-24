# Write your solution here
def column_correct(sudoku: list, column_no: int) -> bool:
    seen = []
    for row in sudoku:
        num = row[column_no]
        if num != 0:  # Skip empty cells
            if num in seen:
                return False
            seen.append(num)
    return True
# Write your solution here
def row_correct(sudoku, row_no):
    seen = []
    for num in sudoku[row_no]:
        if num != 0:
            if num in seen:
                return False
            seen.append(num)
    return True

def column_correct(sudoku, col_no):
    seen = []
    for row in sudoku:
        num = row[col_no]
        if num != 0:
            if num in seen:
                return False
            seen.append(num)
    return True

def block_correct(sudoku, row_no, column_no):
    seen = []
    for r in range(row_no, row_no + 3):
        for c in range(column_no, column_no + 3):
            num = sudoku[r][c]
            if num != 0:
                if num in seen:
                    return False
                seen.append(num)
    return True

def sudoku_grid_correct(sudoku):
    # Check all rows
    for row in range(9):
        if not row_correct(sudoku, row):
            return False

    # Check all columns
    for col in range(9):
        if not column_correct(sudoku, col):
            return False

    # Check all 3x3 blocks
    for row in range(0, 9, 3):
        for col in range(0, 9, 3):
            if not block_correct(sudoku, row, col):
                return False

    return True
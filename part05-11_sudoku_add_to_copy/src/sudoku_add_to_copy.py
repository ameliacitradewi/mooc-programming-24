# Write your solution here
def copy_and_add(sudoku: list, row_no: int, column_no: int, number: int) -> list:
    # Create a deep copy of the sudoku grid
    new_sudoku = [row[:] for row in sudoku]
    
    # Add the number to the specified location
    new_sudoku[row_no][column_no] = number
    
    return new_sudoku

def print_sudoku(sudoku: list):
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0:
                print("_", end=" ")
            else:
                print(sudoku[i][j], end=" ")
            if (j + 1) % 3 == 0 and j < 8:
                print(" ", end="")
        print()
        if (i + 1) % 3 == 0 and i < 8:
            print()

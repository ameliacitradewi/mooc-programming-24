# Write your solution here
def print_sudoku(sudoku: list):
    for i in range(len(sudoku)):
        if i % 3 == 0 and i != 0:
            print()  # Print a blank line to separate 3x3 blocks vertically
        for j in range(len(sudoku[i])):
            if j % 3 == 0 and j != 0:
                print(" ", end="")  # Separate 3x3 blocks horizontally
            if sudoku[i][j] == 0:
                print("_", end=" ")
            else:
                print(sudoku[i][j], end=" ")
        print()  # Move to the next line after each row

def add_number(sudoku: list, row_no: int, column_no: int, number: int):
    if 0 <= row_no < 9 and 0 <= column_no < 9 and 1 <= number <= 9:
        sudoku[row_no][column_no] = number
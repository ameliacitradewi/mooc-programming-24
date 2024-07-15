# Write your solution here
def chessboard(size):
    row = 0
    while row < size:
        col = 0
        line = ""
        while col < size:
            if (row + col) % 2 == 0:
                line += "1"
            else:
                line += "0"
            col += 1
        print(line)
        row += 1
        
# Testing the function
if __name__ == "__main__":
    chessboard(3)

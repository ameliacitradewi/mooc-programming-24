# Copy here code of line function from previous exercise
def line(number, teks):
    if teks == "":
        teks += "*"
    else:
        teks = teks[:1]
    print(teks * number)

def square_of_hashes(size):
    counter = size
    while counter > 0:
        line(size, "#")
        counter -= 1
        
    # You should call function line here with proper parameters
    

# You can test your function by calling it within the following block
if __name__ == "__main__":
    square_of_hashes(5)

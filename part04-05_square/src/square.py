# Copy here code of line function from previous exercise
def line(number, teks):
    if teks == "":
        teks += "*"
    else:
        teks = teks[:1]
    print(teks * number)

def square(size, character):
    # You should call function line here with proper parameters
    counter = size
    while counter > 0:
        line(size, character)
        counter -= 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    square(5, "x")
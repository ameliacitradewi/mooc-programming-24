# Copy here code of line function from previous exercise and use it in your solution
def line(number, teks):
    if teks == "":
        teks += "*"
    else:
        teks = teks[:1]
    print(teks * number)

def shape(jumlahkarakter, chartriangle, barispersegi, charpersegi):
    counter = 1
    while counter <= jumlahkarakter:
        line(counter, chartriangle)
        counter += 1
    row = 1
    while row <= barispersegi:
        line(jumlahkarakter, charpersegi)
        row += 1
    
# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(5, "x", 2, "o")
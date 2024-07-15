# Write your solution here
def line(number, teks):
    if teks == "":
        teks += "*"
    else:
        teks = teks[:1]
    print(teks * number)


# You can test your function by calling it within the following block
if __name__ == "__main__":
    line(5, "x")
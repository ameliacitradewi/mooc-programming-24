# Write your solution here
def spruce(size):
    print("a spruce!")
    for i in range(size):
        # Calculate the number of spaces and stars
        spaces = size - i - 1
        stars = 2 * i + 1
        # Print the line with the calculated spaces and stars
        print(" " * spaces + "*" * stars)
    # Print the trunk of the tree
    print(" " * (size - 1) + "*")     

# You can test your function by calling it within the following block
if __name__ == "__main__":
    spruce(5)
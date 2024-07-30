# Write your solution here
def create_tuple(x: int, y: int, z: int):
    maximum = max(x, y, z)
    minimum = min(x, y, z)
    sum = x + y + z
    final = (minimum, maximum, sum)
    return final

if __name__ == "__main__":
    print(create_tuple(1, 4, 2))

# The first element is the smallest of the arguments
# The second element is the greatest of the arguments
# The third element is the sum of the arguments
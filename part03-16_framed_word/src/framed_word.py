# Write your solution here
import math
word = input("Word:")

length = len(word)
spaceLeft = math.floor((28 - length) / 2)
spaceRight = math.ceil((28 - length) / 2)

print("*" * 30)
print("*" + (" " * spaceLeft) + word + (" " * spaceRight) + "*")
print("*" * 30)
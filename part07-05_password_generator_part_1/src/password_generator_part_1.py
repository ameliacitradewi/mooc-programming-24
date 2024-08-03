# Write your solution here
import random as r
import string as s

def generate_password(length: int):
    letters = s.ascii_lowercase
    password = ""
    for char in range(length):
        password += r.choice(letters)
    return password

# # Example Usage
# for i in range(5):
#   print(generate_password(3))
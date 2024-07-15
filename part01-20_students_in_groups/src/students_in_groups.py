# Write your solution here
import math

student = int(input("How many students on the course? "))
group = int(input("Desired group size? "))
print(f"Number of groups formed: {math.ceil(student / group)}")
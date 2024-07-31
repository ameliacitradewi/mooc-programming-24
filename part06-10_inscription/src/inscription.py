# Write your solution here
name = input()
name_file = input()

with open(name_file, 'w') as file:
    file.write(f"Hi {name}, we hope you enjoy learning Python with us! Best, Mooc.fi Team")
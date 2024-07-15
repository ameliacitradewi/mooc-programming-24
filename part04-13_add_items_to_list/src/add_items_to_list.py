# Write your solution here
times = int(input("How many items:"))
my_list = []

for i in range(times):
    number = int(input(f"Item {i + 1}: "))
    my_list.append(number)

print(my_list)
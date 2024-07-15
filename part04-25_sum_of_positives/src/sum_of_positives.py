# Write your solution here
def sum_of_positives(my_list):
    result = sum(i for i in my_list if i > 0)
    return result

# # Write your solution here (another way, also works)
# def sum_of_positives(my_list):
#     positive_list = []
#     for i in my_list:
#         if i > 0:
#             positive_list.append(i)
#     result = sum(positive_list)
#     return result
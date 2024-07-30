# write your solution here
#     with open("{filename}") as file:
#         lst = [int(data) for data in file]
#         # for data in file:
#         #     data = data.replace("\n", "")
#         #     lst.append(data)
#         print(max(lst))

def largest():
    try:
        with open("numbers.txt") as file:
            lst = [int(data) for data in file]
            return max(lst)
    except Exception:
        print("Error!")
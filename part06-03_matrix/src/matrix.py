# write your solution here
def read_file(file_name = "matrix.txt"):
    new_list = []
    with open(file_name) as file:
        for line in file:
            line = line.replace("\n", "").split(",")
            row = list(map(int, line))
            new_list.append(row)
    return new_list

def matrix_sum():
    lists = read_file()
    result_sum = sum(sum(row) for row in lists)
    return result_sum

def matrix_max():
    lists = read_file()
    max_value = max(max(row) for row in lists)
    return max_value

def row_sums():
    lists = read_file()
    list_sums = []
    for row in lists:
        list_sums.append(sum(row))
    return list_sums

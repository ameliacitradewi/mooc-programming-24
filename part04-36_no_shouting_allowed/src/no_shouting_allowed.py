# Write your solution here
def no_shouting(my_list):
    no_upper = []
    for i in my_list:
        if i.isupper():
            continue
        else:
            no_upper.append(i)
    return no_upper
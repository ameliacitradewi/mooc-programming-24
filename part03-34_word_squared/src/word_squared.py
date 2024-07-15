# Write your solution here
def squared(input_string, input_integer):
    text = input_string * int((input_integer * input_integer))
    i = 0
    j = input_integer
    counter = 1
    while counter <= input_integer:
        print(text[i:j])
        i += input_integer
        j += input_integer
        counter += 1
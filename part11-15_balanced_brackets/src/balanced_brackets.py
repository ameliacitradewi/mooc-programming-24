# WRITE YOUR SOLUTION HERE:
def balanced_brackets(my_string: str) -> bool:
    def is_balanced(brackets):
        # Base case: If the string is empty, it's balanced
        if not brackets:
            return True

        # Check if the first character is an opening bracket
        if not brackets[0] in '([':
            return False

        # Check if the last character is a closing bracket that matches the first
        if not (brackets[0] == '(' and brackets[-1] == ')') and not (brackets[0] == '[' and brackets[-1] == ']'):
            return False
            
        # Remove the first and last characters and recurse
        return is_balanced(brackets[1:-1])

    # Filter out non-bracket characters
    filtered_string = ''.join(char for char in my_string if char in '()[]')
    return is_balanced(filtered_string)


# Test cases
ok = balanced_brackets("([([])])")
print(ok)  # True

ok = balanced_brackets("(python version [3.7]) please use this one!")
print(ok)  # True

ok = balanced_brackets("(()]")
print(ok)  # False

ok = balanced_brackets("([bad egg)]")
print(ok)  # False
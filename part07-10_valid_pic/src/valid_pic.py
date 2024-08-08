# Write your solution here
import datetime

def is_it_valid(pic: str) -> bool:
    if len(pic) != 11:
        return False
    
    # Extract parts of the PIC
    date_part = pic[:6]
    century_marker = pic[6]
    personal_identifier = pic[7:10]
    control_character = pic[10]
    
    # Validate the date part
    day = int(date_part[:2])
    month = int(date_part[2:4])
    year = int(date_part[4:6])
    
    # Determine the full year based on the century marker
    if century_marker == '+':
        year += 1800
    elif century_marker == '-':
        year += 1900
    elif century_marker == 'A':
        year += 2000
    else:
        return False
    
    # Check if the date is valid
    try:
        datetime.datetime(year, month, day)
    except ValueError:
        return False
    
    # Validate the control character
    control_string = "0123456789ABCDEFHJKLMNPRSTUVWXY"
    nine_digit_number = int(date_part + personal_identifier)
    remainder = nine_digit_number % 31
    expected_control_character = control_string[remainder]
    
    return control_character == expected_control_character

# # Test cases
# print(is_it_valid("230827-906F
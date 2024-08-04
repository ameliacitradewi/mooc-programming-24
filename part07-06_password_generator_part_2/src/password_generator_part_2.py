# Write your solution here
import random
import string

def generate_strong_password(length, include_numbers, include_specials):  
    # Define character sets
    lowercase = string.ascii_lowercase
    numbers = string.digits
    specials = "!?=+-()#"
    
    # Ensure the password contains at least one lowercase letter
    password_chars = [random.choice(lowercase)]
    
    # Add at least one number if required
    if include_numbers:
        password_chars.append(random.choice(numbers))
    
    # Add at least one special character if required
    if include_specials:
        password_chars.append(random.choice(specials))
    
    # Fill the rest of the password length with random choices from the allowed sets
    all_allowed_chars = lowercase
    if include_numbers:
        all_allowed_chars += numbers
    if include_specials:
        all_allowed_chars += specials
    
    while len(password_chars) < length:
        password_chars.append(random.choice(all_allowed_chars))
    
    # Shuffle the list to ensure randomness
    random.shuffle(password_chars)
    
    # Join the list into a string to form the final password
    return ''.join(password_chars)

# # Example usage
# for i in range(10):
#   print(generate_strong_password(8, True, True))
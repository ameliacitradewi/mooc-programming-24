# Write your solution here
import string

def separate_characters(my_string: str):
  ascii_letters = string.ascii_letters
  punctuation = string.punctuation
  
  letters = []
  punctuations = []
  others = []
  
  for char in my_string:
      if char in ascii_letters:
          letters.append(char)
      elif char in punctuation:
          punctuations.append(char)
      else:
          others.append(char)
  
  return (''.join(letters), ''.join(punctuations), ''.join(others))

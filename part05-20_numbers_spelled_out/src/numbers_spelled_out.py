# Write your solution here
def dict_of_numbers() -> dict:
  # Basic mappings
  ones = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
  teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
  tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
  
  # Initialize the dictionary
  number_dict = {}
  
  # Fill the dictionary with numbers from 0 to 99
  for i in range(100):
      if i < 10:
          number_dict[i] = ones[i]
      elif 10 <= i < 20:
          number_dict[i] = teens[i - 10]
      else:
          ten_part = tens[i // 10]
          one_part = ones[i % 10]
          if i % 10 == 0:
              number_dict[i] = ten_part
          else:
              number_dict[i] = f"{ten_part}-{one_part}"
  
  return number_dict

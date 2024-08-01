# Write your solution here
import re

def is_valid_week(week):
  return re.match(r"week \d+$", week) is not None
  # check if the week part matches the format where x is a positive integer

def is_valid_numbers(numbers):
  if len(numbers) != 7:
      return False
  try:
      num_set = set()
      for num in numbers:
          n = int(num)
          if n < 1 or n > 39 or n in num_set:
              return False
          num_set.add(n)
      return True
  except ValueError:
      return False

def filter_incorrect():
  with open("lottery_numbers.csv", "r") as infile, open("correct_numbers.csv", "w") as outfile:
      for line in infile:
          line = line.strip()
          if not line:
              continue
          parts = line.split(";")
          if len(parts) != 2:
              continue
          week, numbers = parts
          numbers = numbers.split(",")
                    
          if is_valid_week(week) and is_valid_numbers(numbers):
              outfile.write(line + "\n")
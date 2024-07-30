# Write your solution here
def read_input(prompt: str, lower_bound: int, upper_bound: int):
  while True:
      user_input = input(prompt)
      try:
          user_input = int(user_input)
          if lower_bound <= user_input <= upper_bound:
              return user_input
          else:
              print(f"You must type in an integer between {lower_bound} and {upper_bound}")
      except ValueError:
          print(f"You must type in an integer between {lower_bound} and {upper_bound}")

# Example usage
# number = read_input("Please type in a number: ", 5, 10)
# print("You typed in:", number)

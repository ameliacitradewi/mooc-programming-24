# Write your solution here
import random

def roll(die: str) -> int:
  dice = {
      "A": [3, 3, 3, 3, 3, 6],
      "B": [2, 2, 2, 5, 5, 5],
      "C": [1, 4, 4, 4, 4, 4]
  }
  
  if die in dice:
      return random.choice(dice[die])
  else:
      raise ValueError("Invalid die specified. Choose 'A', 'B', or 'C'.")

def play(die1: str, die2: str, times: int) -> tuple:
  die1_wins = 0
  die2_wins = 0
  ties = 0
  
  for _ in range(times):
      roll1 = roll(die1)
      roll2 = roll(die2)
      
      if roll1 > roll2:
          die1_wins += 1
      elif roll2 > roll1:
          die2_wins += 1
      else:
          ties += 1
  
  return (die1_wins, die2_wins, ties)

# # Example usage:
# for i in range(20):
#   print(roll("A"), " ", end="")
# print()
# for i in range(20):
#   print(roll("B"), " ", end="")
# print()
# for i in range(20):
#   print(roll("C"), " ", end="")
# print()

# result = play("A", "C", 1000)
# print(result)
# result = play("B", "B", 1000)
# print(result)